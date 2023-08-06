# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from pydantic import BaseModel
from typing import Any, Generator, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.utils.functions.dict import dget, dset


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound="Instance")


class Instance(BaseModel):
    """A utility class that represents Python object instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __REPR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        """Representation Method"""

        # Get representation
        representation = self.__class__.__name__

        # Add angle brackets to representation
        representation = f"<{representation}: {self.__str__()}>"

        # Return representation
        return representation

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FROM DICT
    # └─────────────────────────────────────────────────────────────────────────────────

    @classmethod
    def from_dict(cls: type[T], data: Any, where: dict[str, str] | None = None) -> T:
        """Initializes an instance from a dictionary"""

        # Initialize object
        obj = data

        # Check if data is a dictionary
        if isinstance(data, dict):
            # Initialize object
            obj = {}

            # Iterate over where
            for path_to_set, path_to_get in (where or {}).items():
                # Remap data
                dset(obj, path_to_set, dget(data, path_to_get))

        # Initialize instance
        instance = cls.parse_obj(obj)

        # Return instance
        return instance

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FROM LIST
    # └─────────────────────────────────────────────────────────────────────────────────

    @classmethod
    def from_list(
        cls: type[T], data: Any, where: dict[str, str] | None = None
    ) -> Generator[T, None, None]:
        """Yields instances from a list of dictionaries"""

        # Iterate over data
        for item in data:
            # Yield instance
            yield cls.from_dict(item, where=where)
