# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset import Asset
from doji.core.utils.classes.instances import Instances


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ASSET INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound=Asset)


class AssetInstances(Instances[T]):
    """A utility class that represents a collection of Asset instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET INSTANCE KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_instance_key(self, instance: T) -> int | str:
        """Returns the instance key"""

        # Return instance key
        return instance.code
