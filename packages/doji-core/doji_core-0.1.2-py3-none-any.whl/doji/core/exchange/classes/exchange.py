# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.api.mixins.api_mixin import APIMixin
from doji.core.asset.classes.asset import Asset
from doji.core.asset.classes.asset_pair import AssetPair
from doji.core.asset.mixins.assets_mixin import AssetsMixin
from doji.core.asset.mixins.asset_pairs_mixin import AssetPairsMixin

if TYPE_CHECKING:
    from doji.core.types import Args, Kwargs


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ EXCHANGE
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound=Asset)
U = TypeVar("U", bound=AssetPair[Any])


class Exchange(APIMixin, AssetsMixin[T], AssetPairsMixin[U]):
    """A utility class that represents exchanges"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of key
    KEY: str

    # Declare type of name
    NAME: str

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Args, **kwargs: Kwargs) -> None:
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def key(self) -> str:
        """Returns the key of the exchange"""

        # Return key
        return self.KEY

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ NAME
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def name(self) -> str:
        """Returns the name of the exchange"""

        # Return name
        return self.NAME
