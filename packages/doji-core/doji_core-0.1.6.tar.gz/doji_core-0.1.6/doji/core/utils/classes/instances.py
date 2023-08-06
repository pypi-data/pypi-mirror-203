# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Generic, Iterator, TypeVar


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────

# Declare a TypeVar to represent the instance class
T = TypeVar("T")


class Instances(Generic[T]):
    """A utility class that represents a collection of Python object instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of instances by key
    _instances_by_key: dict[int | str, T]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self) -> None:
        """Init Method"""

        # Initialize classes by key
        self._instances_by_key = {}

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __ITER__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __iter__(self) -> Iterator[T]:
        """Iter Method"""

        # Iterate over instances
        for instance in self._instances_by_key.values():
            # Yield instance
            yield instance

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __LEN__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __len__(self) -> int:
        """Len Method"""

        # Return length of instances
        return len(self._instances_by_key)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __REPR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        """Representation Method"""

        # Define threshold
        threshold = 20

        # Get instance count
        count = len(self)

        # Initialize representation to class name
        representation = self.__class__.__name__

        # Add count to representation
        representation += f": {count}"

        # Initialize instances
        instances: list[str] = []

        # Iterate over instances
        for instance in self:
            # Break if length of instances is greater than or equal to threshold
            if len(instances) >= threshold:
                break

            # Append instance representation to instances
            instances.append(instance.__repr__())

        # Check if there are more than n instances total
        if count > threshold:
            # Add truncation message to instances list
            instances.append("...(remaining elements truncated)... ")

        # Add instances to representation
        representation = f"{representation} {'[' + ', '.join(instances) + ']'}"

        # Add angle brackets to the representation
        representation = f"<{representation}>"

        # Return representation
        return representation

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ADD
    # └─────────────────────────────────────────────────────────────────────────────────

    def add(self, instance: T) -> None:
        """Adds an instance to the collection"""

        # Get instance key
        instance_key = self.get_instance_key(instance)

        # Add instance to collection
        self._instances_by_key[instance_key] = instance

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET INSTANCE KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_instance_key(self, instance: T) -> int | str:
        """Returns the instance key"""

        # Return instance key
        return id(instance)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE INSTANCE
    # └─────────────────────────────────────────────────────────────────────────────────

    def update_instance(self, existing_instance: T, new_instance: T) -> None:
        """Updates an existing instance with a new instance"""

        # Update existing instance with new instance
        existing_instance.__dict__.update(new_instance.__dict__)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE OR ADD
    # └─────────────────────────────────────────────────────────────────────────────────

    def update_or_add(self, instance: T) -> None:
        """Updates or adds an instance to the collection"""

        # Get instance key
        instance_key = self.get_instance_key(instance)

        # Check if instance ID not in instances by key
        if instance_key not in self._instances_by_key:
            # Add instance to collection
            return self.add(instance)

        # Get existing instance
        existing_instance = self._instances_by_key[instance_key]

        # Update existing instance
        self.update_instance(existing_instance, instance)
