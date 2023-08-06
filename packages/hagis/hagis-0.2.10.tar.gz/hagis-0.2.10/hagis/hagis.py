from datetime import datetime
from hashlib import md5
from itertools import islice
from json import dumps, loads
from requests import post
from time import time
from types import SimpleNamespace
from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, Tuple, Type, TypeVar, Union

T = TypeVar("T")

class Layer(Generic[T]):
    def __init__(self, layer_url: str, model: Type[T] = SimpleNamespace, oid_field: str = "objectid", shape_property_name: str = "shape", **mapping: str) -> None:
        """ Creates a new instance of the Layer class.

        Args:
            layer_url (str): Layer url (e.g. .../FeatureServer/0).
            model (Type[T], optional): Model to map to.  Defaults to SimpleNamespace.
            oid_field (str, optional): Name of the Object ID field.  Defaults to "objectid".
            shape_property_name (str, optional): Name of the shape property.  Defaults to "shape".
        """
        self._layer_url = layer_url
        self._model = model
        self._oid_field = oid_field
        self._shape_property_name = shape_property_name
        self._shape_property_type = None
        self._unknown_shape_types = [Any, object, SimpleNamespace]
        self._fields: Dict[str, str] = {}
        self._generate_token: Callable[[], str] = lambda: ""
        self._is_dynamic = model == SimpleNamespace

        if self._is_dynamic:
            return

        # List of custom mapping properties that have been handled.
        mapped: List[str] = []

        for type in reversed(model.__mro__):
            if hasattr(type, "__annotations__"):
                for property_name, property_type in type.__annotations__.items():
                    key = property_name.lower()

                    if property_name in mapping:
                        self._fields[key] = mapping[property_name]
                        mapped.append(property_name)
                    else:
                        self._fields[key] = property_name

                    if key == shape_property_name.lower():
                        self._shape_property_name = property_name
                        self._shape_property_type = property_type

        # Add custom properties that have not been handled as dynamically handled propeties.
        for property, field in mapping.items():
            if property not in mapped:
                self._fields[property.lower()] = field

    _token_cache: Dict[Tuple[str, str], Tuple[str, int]] = {}

    def set_token_generator(self, username: str, password: str, referer: str = "", generate_token_url: str = "https://www.arcgis.com/sharing/generateToken", **kwargs: Any) -> None:
        kwargs["username"] = username
        kwargs["password"] = password
        kwargs["referer"] = referer
        kwargs["client"] = "referer" if referer else "ip" if "ip" in kwargs else "requestip"

        key = generate_token_url, md5(dumps(kwargs).encode("utf-8")).hexdigest()

        def generate_token() -> str:
            if key not in Layer._token_cache:
                Layer._token_cache[key] = "", 0

            # Get the cached token and its expiry.
            token, expiration_seconds = Layer._token_cache[key]

            # Renew if less than a minute left.
            if expiration_seconds - time() < 60:
                obj = self._post(generate_token_url, **kwargs)
                token, expiration_seconds = obj.token, obj.expires / 1000
                Layer._token_cache[key] = token, expiration_seconds

            return token

        self._generate_token = generate_token

    def set_token(self, token: str) -> None:
        self._generate_token = lambda: token

    def query(self, where_clause: str = "1=1", resultRecordCount: int = 10000, **kwargs: Any) -> Iterable[T]:
        if self._is_dynamic:
            # If dynamic, request all fields.
            fields = "*"
        else:
            # Otherwise, request only what is used by the model.
            fields = ",".join([f for (_, f) in self._fields.items() if f != self._shape_property_name.lower()])
            if not self._shape_property_name:
                kwargs["returnGeometry"] = False

        # Prevent throwing an exception when zero record is requested.
        kwargs["resultRecordCount"] = resultRecordCount if resultRecordCount else 1

        for row in islice(self._query(where_clause, fields, **kwargs), resultRecordCount):
            if self._is_dynamic:
                yield row  # type: ignore
            else:
                dictionary = {property: getattr(row, field) for (property, field) in self._fields.items()}
                if hasattr(self._model, "__dataclass_fields__"):
                    # Support for dataclasses.
                    item = self._model(*dictionary.values())
                else:
                    # Normal classes require the parameterless constructor.
                    item = self._model()
                    for property_name, property_value in dictionary.items():
                        setattr(item, property_name, property_value)
                yield item

    def count(self, where_clause: str = "1=1") -> int:
        obj = self._call("query", where=where_clause, returnCountOnly=True)
        return obj.count

    def find(self, oid: int, **kwargs: Any) -> Optional[T]:
        items = [item for item in self.query(f"{self._oid_field}={oid}", **kwargs)]
        if items:
            return items[0]

    def apply_edits(self, adds: Optional[List[T]] = None, updates: Optional[List[T]] = None, deletes: Union[List[int], List[str], None] = None, **kwargs: Any) -> SimpleNamespace:
        adds_json = "" if adds is None else dumps([self._to_dict(x) for x in adds])
        updates_json = "" if updates is None else dumps([self._to_dict(x) for x in updates])
        deletes_json = "" if deletes is None else dumps([x for x in deletes])
        return self._call("applyEdits", adds=adds_json, updates=updates_json, deletes=deletes_json, **kwargs)

    def insert(self, items: List[T], **kwargs: Any) -> List[int]:
        result = self.apply_edits(adds=items, **kwargs)
        return [x.objectId for x in result.addResults]

    def update(self, items: List[T], **kwargs: Any) -> None:
        self.apply_edits(updates=items, **kwargs)

    def delete(self, where_clause: str, **kwargs: Any) -> None:
        self._call("deleteFeatures", where=where_clause, **kwargs)

    def _to_dict(self, item: T) -> Dict[str, Any]:
        dictionary: Dict[str, Any] = {}
        attributes: Dict[str, Any] = {}

        dictionary["attributes"] = attributes

        for key, value in item.__dict__.items():
            property = key.lower()
            field = self._fields[property]
            if property == self._shape_property_name:
                dictionary["geometry"] = value.__dict__
            elif isinstance(value, datetime):
                attributes[field] = int((value - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
            else:
                attributes[field] = value

        return dictionary

    def _post(self, url: str, **kwargs: Any) -> SimpleNamespace:
        kwargs["f"] = "json"
        response = post(url, kwargs)
        obj = loads(response.text, object_hook=lambda x: SimpleNamespace(**x))

        if hasattr(obj, "error"):
            raise Exception(obj.error.message)

        return obj

    def _call(self, method: str, **kwargs: Any) -> SimpleNamespace:
        kwargs["token"] = self._generate_token()
        return self._post(f"{self._layer_url}/{method}", **kwargs)

    def _get_rows(self, where_clause: str, fields: str, **kwargs: Any) -> Tuple[List[SimpleNamespace], bool]:
        obj = self._call("query", where=where_clause, outFields=fields, **kwargs)
        date_fields = [f.name for f in obj.fields if f.type == "esriFieldTypeDate"] if hasattr(obj, "fields") else []

        if date_fields:
            for f in obj.features:
                for key, value in f.attributes.__dict__.items():
                    if key in date_fields and value:
                        f.attributes.__dict__[key] = datetime.fromtimestamp(value / 1000)

        return (obj.features, obj.exceededTransferLimit if hasattr(obj, "exceededTransferLimit") else False)

    def _get_oids(self, where_clause: str) -> List[int]:
        obj = self._call("query", where=where_clause, returnIdsOnly="true")
        return obj.objectIds

    def _map(self, row: SimpleNamespace) -> SimpleNamespace:
        if not hasattr(row, "geometry"):
            return row.attributes

        if self._shape_property_type is None or self._shape_property_type in self._unknown_shape_types:
            shape = row.geometry
        else:
            shape = self._shape_property_type()
            shape.__dict__ = row.geometry.__dict__

        return SimpleNamespace(**row.attributes.__dict__, **{self._shape_property_name: shape})

    def _query(self, where_clause: str, fields: str, **kwargs: Any) -> Iterable[SimpleNamespace]:
        def get_rows(where_clause: str):
            return self._get_rows(where_clause, fields, **kwargs)

        rows, exceededTransferLimit = get_rows(where_clause)

        for row in rows:
            yield self._map(row)

        if exceededTransferLimit:
            size = len(rows)
            oids = self._get_oids(where_clause)
            for n in range(size, len(oids), size):
                more_where_clause = f"{self._oid_field} IN ({','.join(map(str, oids[n:n+size]))})"
                more_rows, _ = get_rows(more_where_clause)
                for row in more_rows:
                    yield self._map(row)


class Point:
    x: float
    y: float

class Multipoint:
    points: List[List[float]]

class Polyline:
    paths: List[List[List[float]]]

class Polygon:
    rings: List[List[List[float]]]
