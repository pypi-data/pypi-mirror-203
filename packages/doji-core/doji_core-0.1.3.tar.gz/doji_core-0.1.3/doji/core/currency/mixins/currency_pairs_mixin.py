# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import logging

from typing import Any, AsyncGenerator, Coroutine, Generator

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.mixins.asset_pairs_mixin import AssetPairsMixin
from doji.core.currency.classes.currency_pair import CurrencyPair
from doji.core.currency.classes.currency_pair_instances import CurrencyPairInstances


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY PAIRS MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyPairsMixin(AssetPairsMixin[CurrencyPair]):
    """A mixin for classes with currency pairs-related attributes and methods"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of asset pairs
    asset_pairs: CurrencyPairInstances

    # Declare type of asset pairs async
    asset_pairs_async: Coroutine[Any, Any, CurrencyPairInstances]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CURRENCY PAIRS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def currency_pairs(self) -> CurrencyPairInstances:
        """Returns a collection of CurrencyPair instances"""

        # Return the asset pairs of the currency exchange
        return self.asset_pairs

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CURRENCIES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def currency_pairs_async(self) -> CurrencyPairInstances:
        """Returns a collection of CurrencyPair instances"""

        # Return the asset pairs of the currency exchange
        return await self.asset_pairs_async

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSET PAIRS
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_asset_pairs(self) -> CurrencyPairInstances:
        """Fetches a collection of CurrencyPair instances from an API synchronously"""

        # Initialize asset pairs
        asset_pairs = CurrencyPairInstances()

        # Iterate over currency pairs
        for currency_pair in self.fetch_currency_pairs_from_api():
            # Add currency pairs to asset pairs
            asset_pairs.add(currency_pair)

        # Cache asset pairs
        self._asset_pairs = asset_pairs

        # Return asset pairs
        return asset_pairs

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSET PAIRS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_asset_pairs_async(self) -> CurrencyPairInstances:
        """Fetches a collection of CurrencyPair instances from an API asynchronously"""

        # Initialize asset pairs
        asset_pairs = CurrencyPairInstances()

        # Iterate over currency pairs
        async for currency_pair in self.fetch_currency_pairs_from_api_async():
            # Add currency pairs to asset pairs
            asset_pairs.add(currency_pair)

        # Cache asset pairs
        self._asset_pairs = asset_pairs

        # Return asset pairs
        return asset_pairs

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCY PAIRS
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_currency_pairs(self) -> CurrencyPairInstances:
        """Fetches a collection of CurrencyPair instances synchronously"""

        # Fetch and return asset pairs
        return self.fetch_asset_pairs()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCY PAIRS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_currency_pairs_async(self) -> CurrencyPairInstances:
        """Fetches a collection of CurrencyPair instances asynchronously"""

        # Fetch and return asset pairs
        return await self.fetch_asset_pairs_async()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCY PAIRS FROM API
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_currency_pairs_from_api(self) -> Generator[CurrencyPair, None, None]:
        """Fetches a collection of CurrencyPair instances from an API synchronously"""

        # Initialize currency pairs
        currency_pairs: list[CurrencyPair] = []

        # Iterate over currency pairs
        for currency_pair in currency_pairs:
            # Yield currency pair
            yield currency_pair

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCY PAIRS FROM API ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_currency_pairs_from_api_async(
        self,
    ) -> AsyncGenerator[CurrencyPair, None]:
        """Fetches a collection of CurrencyPair instances from an API asynchronously"""

        # Get class name
        class_name = self.__class__.__name__

        # Log a warning
        logging.warning(
            f"{class_name}.fetch_currency_pairs_from_api_async not implemented; "
            f"using {class_name}.fetch_currency_pairs_from_api.\n"
        )

        # Iterate over currency pairs
        for currency_pair in self.fetch_currency_pairs_from_api():
            # Yield currency pair
            yield currency_pair
