# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTANCE
# └─────────────────────────────────────────────────────────────────────────────────────


class Instance:
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
