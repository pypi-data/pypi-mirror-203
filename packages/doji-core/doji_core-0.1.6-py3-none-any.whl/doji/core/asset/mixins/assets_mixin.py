# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TYPE_CHECKING, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset import Asset

if TYPE_CHECKING:
    from doji.core.types import Args, Kwargs
    from doji.core.asset.classes.asset_instances import AssetInstances


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ASSETS MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────

T = TypeVar("T", bound=Asset)


class AssetsMixin(Generic[T], ABC):
    """A mixin for classes with assets-related attributes and methods"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of assets cache
    _assets: AssetInstances[T] | None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Args, **kwargs: Kwargs) -> None:
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Initialize assets cache to None
        self._assets = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ASSETS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def assets(self) -> AssetInstances[T]:
        """Returns a collection of assets"""

        # Get cached assets
        _assets = self._assets

        # Check if cached assets is None
        if _assets is None:
            # Fetch assets
            _assets = self.fetch_assets()

            # Set cached assets
            self._assets = _assets

        # Return cached assets
        return _assets

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ASSETS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def assets_async(self) -> AssetInstances[T]:
        """Returns a collection of assets"""

        # Get cached assets
        _assets = self._assets

        # Check if cached assets is None
        if _assets is None:
            # Fetch assets
            _assets = await self.fetch_assets_async()

            # Set cached assets
            self._assets = _assets

        # Return cached assets
        return _assets

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ BASES
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    @abstractmethod
    def bases(self) -> AssetInstances[T]:
        """Returns a collection of base assets synchronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ BASES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    @abstractmethod
    async def bases_async(self) -> AssetInstances[T]:
        """Returns a collection of base assets asynchronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ QUOTES
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    @abstractmethod
    def quotes(self) -> AssetInstances[T]:
        """Returns a collection of quote assets synchronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ QUOTES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    @abstractmethod
    async def quotes_async(self) -> AssetInstances[T]:
        """Returns a collection of quote assets asynchronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSETS
    # └─────────────────────────────────────────────────────────────────────────────────

    @abstractmethod
    def fetch_assets(self) -> AssetInstances[T]:
        """Fetches a collection of assets syncronously"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSETS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @abstractmethod
    async def fetch_assets_async(self) -> AssetInstances[T]:
        """Fetches a collection of assets asyncronously"""
