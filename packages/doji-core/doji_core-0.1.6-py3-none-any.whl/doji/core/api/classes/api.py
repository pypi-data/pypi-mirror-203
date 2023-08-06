# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import aiohttp
import posixpath
import requests

from json.decoder import JSONDecodeError
from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from doji.core.api.classes.api_response import APIResponse


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ API
# └─────────────────────────────────────────────────────────────────────────────────────


class API:
    """A utility class that represents API clients"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, base_url: str) -> None:
        """Init Method"""

        # Set the base URL
        self.base_url = base_url

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CONSTRUCT URL
    # └─────────────────────────────────────────────────────────────────────────────────

    def construct_url(self, *route: str, base_url: str | None = None) -> str:
        """Constructs a URL from the base URL and endpoint"""

        # Get base URL
        base_url = base_url or self.base_url

        # Construct URL
        url = posixpath.join(base_url, *route)

        # Return URL
        return url

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET
    # └─────────────────────────────────────────────────────────────────────────────────

    def get(
        self,
        *route: str,
        params: dict[str, Any] | None = None,
        base_url: str | None = None
    ) -> APIResponse:
        """Makes a synchronous HTTP GET request"""

        # Initialize params
        params = params or {}

        # Construct URL
        url = self.construct_url(*route, base_url=base_url)

        # Make GET request
        response = requests.get(url, **params)

        # Initialize try-except block
        try:
            # Get JSON data
            json = response.json()

        # Handle JSONDecodeError
        except JSONDecodeError:
            # Set JSON data to None
            json = None

        # Return API response
        return APIResponse(response=response, json=json)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET ASYNC
    # └─────────────────────────────────────────────────────────────────────────────────

    async def get_async(
        self,
        *route: str,
        params: dict[str, Any] | None = None,
        base_url: str | None = None
    ) -> APIResponse:
        """Makes an asynchronous HTTP GET request"""

        # Initialize params
        params = params or {}

        # Construct URL
        url = self.construct_url(*route, base_url=base_url)

        # Make GET request
        async with aiohttp.ClientSession() as session:
            # Get response
            async with session.get(url, params=params) as response:
                # Initialize try-except block
                try:
                    # Get JSON
                    json = await response.json(content_type=None)

                # Handle JSONDecodeError
                except JSONDecodeError:
                    # Set JSON data to None
                    json = None

        # Return API response
        return APIResponse(response=response, json=json)
