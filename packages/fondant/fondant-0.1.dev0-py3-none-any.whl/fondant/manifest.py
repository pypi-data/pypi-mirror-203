"""This module defines classes to represent a Fondant manifest."""
import copy
import enum
import json
import pkgutil
import types
import typing as t

import jsonschema.exceptions
from jsonschema import Draft4Validator

from fondant.exceptions import InvalidManifest


class Type(enum.Enum):
    """Supported types.

    Based on:
    - https://arrow.apache.org/docs/python/api/datatypes.html#api-types
    - https://pola-rs.github.io/polars/py-polars/html/reference/datatypes.html
    """

    bool: str = "bool"

    int8: str = "int8"
    int16: str = "int16"
    int32: str = "int32"
    int64: str = "int64"

    uint8: str = "uint8"
    uint16: str = "uint16"
    uint32: str = "uint32"
    uint64: str = "uint64"

    float16: str = "float16"
    float32: str = "float32"
    float64: str = "float64"

    decimal: str = "decimal"

    time32: str = "time32"
    time64: str = "time64"
    timestamp: str = "timestamp"

    date32: str = "date32"
    date64: str = "date64"
    duration: str = "duration"

    utf8: str = "utf8"

    binary: str = "binary"

    categorical: str = "categorical"

    list: str = "list"
    struct: str = "struct"


class Field(t.NamedTuple):
    """Class representing a single field or column in a Fondant subset."""

    name: str
    type: Type


class Subset:
    """
    Class representing a Fondant subset.

    Args:
        specification: The part of the manifest json representing the subset
        base_path: The base path which the subset location is defined relative to
    """

    def __init__(self, specification: dict, *, base_path: str) -> None:
        self._specification = specification
        self._base_path = base_path

    @property
    def location(self) -> str:
        """The resolved location of the subset"""
        return self._base_path.rstrip("/") + self._specification["location"]

    @property
    def fields(self) -> t.Mapping[str, Field]:
        """The fields of the subset returned as a immutable mapping."""
        return types.MappingProxyType(
            {
                name: Field(name=name, type=field["type"])
                for name, field in self._specification["fields"].items()
            }
        )

    def add_field(self, name: str, type_: Type) -> None:
        if name in self._specification["fields"]:
            raise ValueError("A field with name {name} already exists")

        self._specification["fields"][name] = {"type": type_.value}

    def remove_field(self, name: str) -> None:
        del self._specification["fields"][name]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._specification!r}"


class Index(Subset):
    """Special case of a subset for the index, which has fixed fields"""

    @property
    def fields(self) -> t.Dict[str, Field]:
        return {
            "id": Field(name="id", type=Type.utf8),
            "source": Field(name="source", type=Type.utf8),
        }


class Manifest:
    """
    Class representing a Fondant manifest

    Args:
        specification: The manifest specification as a Python dict
    """

    def __init__(self, specification: t.Optional[dict] = None) -> None:
        self._specification = copy.deepcopy(specification)
        self._validate_spec()

    def _validate_spec(self) -> None:
        """Validate a manifest specification against the manifest schema

        Raises: InvalidManifest when the manifest is not valid.
        """
        spec_schema = json.loads(pkgutil.get_data("fondant", "schemas/manifest.json"))
        validator = Draft4Validator(spec_schema)
        try:
            validator.validate(self._specification)
        except jsonschema.exceptions.ValidationError as e:
            raise InvalidManifest.create_from(e)

    @classmethod
    def create(cls, *, base_path: str, run_id: str, component_id: str) -> "Manifest":
        """Create an empty manifest

        Args:
            base_path: The base path of the manifest
            run_id: The id of the current pipeline run
            component_id: The id of the current component being executed
        """
        specification = {
            "metadata": {
                "base_path": base_path,
                "run_id": run_id,
                "component_id": component_id,
            },
            "index": {"location": f"/index/{run_id}/{component_id}"},
            "subsets": {},
        }
        return cls(specification)

    @classmethod
    def from_file(cls, path: str) -> "Manifest":
        """Load the manifest from the file specified by the provided path"""
        with open(path, encoding="utf-8") as file_:
            specification = json.load(file_)
            return cls(specification)

    def to_file(self, path) -> None:
        """Dump the manifest to the file specified by the provided path"""
        with open(path, "w", encoding="utf-8") as file_:
            json.dump(self._specification, file_)

    def copy(self):
        """Return a deep copy of itself"""
        return self.__class__(copy.deepcopy(self._specification))

    @property
    def metadata(self) -> dict:
        return self._specification["metadata"]

    def add_metadata(self, key: str, value: t.Any) -> None:
        self.metadata[key] = value

    @property
    def base_path(self) -> str:
        return self.metadata["base_path"]

    @property
    def run_id(self) -> str:
        return self.metadata["run_id"]

    @property
    def component_id(self) -> str:
        return self.metadata["component_id"]

    @property
    def index(self) -> Index:
        return Index(self._specification["index"], base_path=self.base_path)

    @property
    def subsets(self) -> t.Mapping[str, Subset]:
        """The subsets of the manifest as an immutable mapping"""
        return types.MappingProxyType(
            {
                name: Subset(subset, base_path=self.base_path)
                for name, subset in self._specification["subsets"].items()
            }
        )

    def add_subset(self, name: str, fields: t.List[t.Tuple[str, Type]]) -> None:
        if name in self._specification["subsets"]:
            raise ValueError("A subset with name {name} already exists")

        self._specification["subsets"][name] = {
            "location": f"/{name}/{self.run_id}/{self.component_id}",
            "fields": {name: {"type": type_.value} for name, type_ in fields},
        }

    def remove_subset(self, name: str) -> None:
        del self._specification["subsets"][name]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._specification!r}"
