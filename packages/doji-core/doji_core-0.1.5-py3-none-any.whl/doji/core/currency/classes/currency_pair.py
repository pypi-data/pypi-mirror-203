# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset_pair import AssetPair
from doji.core.currency.classes.currency import Currency


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY PAIR
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyPair(AssetPair[Currency]):
    """A utility class that represents currency pairs"""
