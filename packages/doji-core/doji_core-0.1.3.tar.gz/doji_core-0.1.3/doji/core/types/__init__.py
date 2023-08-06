# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.api.classes.api_response import APIResponse  # noqa: F401


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ARGS AND KWARGS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a generic Args type
Args = tuple[Any, ...]

# Define a generic Kwargs type
Kwargs = Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ JSON
# └─────────────────────────────────────────────────────────────────────────────────────

# Define a generic JSON value type
JSONValue = str | int | float | bool | None

# Define a generic JSON dict type
JSONDict = dict[str, JSONValue | "JSON" | list["JSON"]]

# Define a generic JSON array type
JSONArray = list[JSONValue | "JSON" | JSONDict]

# Define a generic JSON type
JSON = JSONValue | JSONDict | JSONArray
