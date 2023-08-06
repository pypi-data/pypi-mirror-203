# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset_pair_instances import AssetPairInstances
from doji.core.currency.classes.currency_pair import CurrencyPair


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY PAIR INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyPairInstances(AssetPairInstances[CurrencyPair]):
    """A utility class that represents a collection of currency pair instances"""
