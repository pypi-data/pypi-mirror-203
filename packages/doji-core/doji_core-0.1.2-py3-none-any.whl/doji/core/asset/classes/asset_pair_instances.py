# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset_pair import AssetPair
from doji.core.utils.classes.instances import Instances


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ASSET PAIR INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound=AssetPair[Any])


class AssetPairInstances(Instances[T]):
    """A utility class that represents a collection of AssetPair instances"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET INSTANCE KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_instance_key(self, instance: T) -> int | str:
        """Returns the instance key"""

        # Return instance key
        return instance.symbol
