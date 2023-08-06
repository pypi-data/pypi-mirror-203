# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from pydantic import BaseModel
from typing import Any, Generator, TypeVar


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

        # Check if data is a dictionary
        if where and isinstance(data, dict):
            # Remap keys
            data = {where.get(key, key): value for key, value in data.items()}

        # Initialize instance
        instance = cls.parse_obj(data)

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
