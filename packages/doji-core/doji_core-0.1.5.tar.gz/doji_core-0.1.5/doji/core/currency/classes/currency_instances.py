# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.asset.classes.asset_instances import AssetInstances
from doji.core.currency.classes.currency import Currency


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY INSTANCES
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyInstances(AssetInstances[Currency]):
    """A utility class that represents a collection of currency instances"""
