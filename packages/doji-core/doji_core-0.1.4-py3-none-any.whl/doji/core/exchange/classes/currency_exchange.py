# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.currency.classes.currency import Currency
from doji.core.currency.classes.currency_pair import CurrencyPair
from doji.core.currency.mixins.currencies_mixin import CurrenciesMixin
from doji.core.currency.mixins.currency_pairs_mixin import CurrencyPairsMixin
from doji.core.exchange.classes.exchange import Exchange


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY EXCHANGE
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyExchange(
    Exchange[Currency, CurrencyPair], CurrenciesMixin, CurrencyPairsMixin
):
    """A utility class that represents currency exchanges"""
