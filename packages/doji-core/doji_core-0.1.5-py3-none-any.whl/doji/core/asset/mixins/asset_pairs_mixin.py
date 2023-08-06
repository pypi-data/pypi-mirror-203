# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset_pair import AssetPair

if TYPE_CHECKING:
    from doji.core.types import Args, Kwargs
    from doji.core.asset.classes.asset_pair_instances import AssetPairInstances


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ASSET PAIRS MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound=AssetPair[Any])


class AssetPairsMixin(Generic[T], ABC):
    """A mixin for classes with asset pairs-related attributes and methods"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of asset pairs cache
    _asset_pairs: AssetPairInstances[T] | None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Args, **kwargs: Kwargs) -> None:
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Initialize asset pairs cache to None
        self._asset_pairs = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ASSET PAIRS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def asset_pairs(self) -> AssetPairInstances[T]:
        """Returns a collection of asset pairs"""

        # Get cached asset_pairs
        _asset_pairs = self._asset_pairs

        # Check if cached asset_pairs is None
        if _asset_pairs is None:
            # Fetch asset_pairs
            _asset_pairs = self.fetch_asset_pairs()

            # Set cached asset_pairs
            self._asset_pairs = _asset_pairs

        # Return cached asset_pairs
        return _asset_pairs

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ASSET PAIRS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def asset_pairs_async(self) -> AssetPairInstances[T]:
        """Returns a collection of asset pairs"""

        # Get cached asset_pairs
        _asset_pairs = self._asset_pairs

        # Check if cached asset_pairs is None
        if _asset_pairs is None:
            # Fetch asset_pairs
            _asset_pairs = await self.fetch_asset_pairs_async()

            # Set cached asset_pairs
            self._asset_pairs = _asset_pairs

        # Return cached asset_pairs
        return _asset_pairs

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSET PAIRS
    # └─────────────────────────────────────────────────────────────────────────────────

    @abstractmethod
    def fetch_asset_pairs(self) -> AssetPairInstances[T]:
        """Fetches a collection of asset pairs syncronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSETS PAIRS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @abstractmethod
    async def fetch_asset_pairs_async(self) -> AssetPairInstances[T]:
        """Fetches a collection of asset pairs asyncronously"""
