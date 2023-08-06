# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import asyncio
import logging

from typing import Any, AsyncGenerator, Coroutine, Generator

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.mixins.assets_mixin import AssetsMixin
from doji.core.currency.classes.currency import Currency
from doji.core.currency.classes.currency_instances import CurrencyInstances
from doji.core.currency.mixins.currency_pairs_mixin import CurrencyPairsMixin


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCIES MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrenciesMixin(AssetsMixin[Currency], CurrencyPairsMixin):
    """A mixin for classes with currencies-related attributes and methods"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of assets
    assets: CurrencyInstances

    # Declare type of assets async
    assets_async: Coroutine[Any, Any, CurrencyInstances]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ BASES
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def bases(self) -> CurrencyInstances:
        """Returns a collection of CurrencyPair base Currency instances synchronously"""

        # Initialize bases
        bases = CurrencyInstances()

        # Iterate over currency pairs
        for currency_pair in self.currency_pairs:
            # Add base to bases
            bases.add(currency_pair.base)

        # Return bases
        return bases

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ BASES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def bases_async(self) -> CurrencyInstances:
        """
        Returns a collection of CurrencyPair base Currency instances asynchronously
        """

        # Initialize bases
        bases = CurrencyInstances()

        # Iterate over currency pairs
        for currency_pair in await self.currency_pairs_async:
            # Add base to bases
            bases.add(currency_pair.base)

        # Return bases
        return bases

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ QUOTES
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def quotes(self) -> CurrencyInstances:
        """
        Returns a collection of CurrencyPair quote Currency instances synchronously
        """

        # Initialize quotes
        quotes = CurrencyInstances()

        # Iterate over currency pairs
        for currency_pair in self.currency_pairs:
            # Add quote to quotes
            quotes.add(currency_pair.quote)

        # Return quotes
        return quotes

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ QUOTES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def quotes_async(self) -> CurrencyInstances:
        """
        Returns a collection of CurrencyPair quote Currency instances asynchronously
        """

        # Initialize quotes
        quotes = CurrencyInstances()

        # Iterate over currency pairs
        for currency_pair in await self.currency_pairs_async:
            # Add quote to quotes
            quotes.add(currency_pair.quote)

        # Return quotes
        return quotes

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CURRENCIES
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def currencies(self) -> CurrencyInstances:
        """Returns a collection of Currency instances"""

        # Return the assets of the currency exchange
        return self.assets

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CURRENCIES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    async def currencies_async(self) -> CurrencyInstances:
        """Returns a collection of Currency instances"""

        # Return the assets of the currency exchange
        return await self.assets_async

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSETS
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_assets(self) -> CurrencyInstances:
        """Fetches a collection of Currency instances from an API synchronously"""

        # Initialize assets
        assets = CurrencyInstances()

        # Iterate over currency pairs
        for currency_pair in self.fetch_currency_pairs():
            # Iterate over base and quote currencies
            for currency in (currency_pair.base, currency_pair.quote):
                # Add currency to assets
                assets.add(currency)

        # Iterate over currencies
        for currency in self.fetch_currencies_from_api():
            # Add currency to assets
            assets.update_or_add(currency)

        # Cache assets
        self._assets = assets

        # Return assets
        return assets

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH ASSETS ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_assets_async(self) -> CurrencyInstances:
        """Fetches a collection of Currency instances from an API asynchronously"""

        # Initialize assets
        assets = CurrencyInstances()

        # Define list currencies helper
        async def list_currencies() -> list[Currency]:
            # Return list of currencies
            return [
                currency async for currency in self.fetch_currencies_from_api_async()
            ]

        # Await currencies and currency pairs
        currencies, currency_pairs = await asyncio.gather(
            list_currencies(), self.fetch_currency_pairs_async()
        )

        # Iterate over currency pairs
        for currency_pair in currency_pairs:
            # Iterate over base and quote currencies
            for currency in (currency_pair.base, currency_pair.quote):
                # Add currency to assets
                assets.add(currency)

        # Iterate over currencies
        for currency in currencies:
            # Add currency to assets
            assets.update_or_add(currency)

        # Cache assets
        self._assets = assets

        # Return assets
        return assets

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCIES
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_currencies(self) -> CurrencyInstances:
        """Fetches a collection of Currency instances synchronously"""

        # Fetch and return assets
        return self.fetch_assets()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCIES ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_currencies_async(self) -> CurrencyInstances:
        """Fetches a collection of Currency instances asynchronously"""

        # Fetch and return assets
        return await self.fetch_assets_async()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCIES FROM API
    # └─────────────────────────────────────────────────────────────────────────────────

    def fetch_currencies_from_api(self) -> Generator[Currency, None, None]:
        """Fetches a collection of Currency instances from an API synchronously"""

        # Initialize currencies
        currencies: list[Currency] = []

        # Iterate over currencies
        for currency in currencies:
            # Yield currency
            yield currency

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FETCH CURRENCIES FROM API ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def fetch_currencies_from_api_async(self) -> AsyncGenerator[Currency, None]:
        """Fetches a collection of Currency instances from an API asynchronously"""

        # Get class name
        class_name = self.__class__.__name__

        # Log a warning
        logging.warning(
            f"{class_name}.fetch_currencies_from_api_async not implemented; "
            f"using {class_name}.fetch_currencies_from_api.\n"
        )

        # Iterate over currencies
        for currency in self.fetch_currencies_from_api():
            # Yield currency
            yield currency
