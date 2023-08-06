# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

import aiohttp
import requests

from typing import TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

if TYPE_CHECKING:
    from doji.core.types import JSON


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ RESPONSE
# └─────────────────────────────────────────────────────────────────────────────────────


class Response:
    """A utility class that represents HTTP responses"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of _object
    _object: requests.Response | aiohttp.ClientResponse

    # Declare type of JSON
    json: JSON

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(
        self, response: requests.Response | aiohttp.ClientResponse, json: JSON = None
    ) -> None:
        """Init Method"""

        # Set response as _object
        self._object = response

        # Set JSON
        self.json = json

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ STATUS CODE
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def status_code(self) -> int:
        """Return the status code of the response object"""

        # Return status code
        return (
            self._object.status_code
            if isinstance(self._object, requests.Response)
            else self._object.status
        )
