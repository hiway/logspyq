"""
Logseq Local API Client.
"""

from json.decoder import JSONDecodeError
from typing import List
from urllib.parse import urljoin as url_join

from asyncgnostic import awaitable
from httpx import Client as HttpxClient
from httpx import AsyncClient as HttpxAsyncClient


class LogseqAPI:
    def __init__(
        self, auth_token: str, endpoint: str = "http://127.0.0.1:12315/"
    ) -> None:
        self.auth_token = auth_token
        self.endpoint = endpoint
        self.url = url_join(endpoint, "/api")
        self.client = HttpxClient()
        self.async_client = HttpxAsyncClient()
        self.headers = {"Authorization": f"Bearer {auth_token}"}

    def _parse_json(self, response) -> [dict|list|str]:
        try:
            return response.json()
        except JSONDecodeError:
            # Some methods, such as "logseq.UI.showMsg" return
            # invalid JSON / unquoted string
            return response.text

    def call(self, method: str, *args: List[str]) -> [dict|list|str]:
        payload = {"method": method, "args": args}
        response = self.client.post(
            self.url,
            headers=self.headers,
            json=payload,
        )
        response.raise_for_status()
        return self._parse_json(response)

    @awaitable(call)
    async def call(self, method: str, *args: List[str]) -> [dict|list|str]:
        payload = {"method": method, "args": args}
        response = await self.async_client.post(
            self.url,
            headers=self.headers,
            json=payload,
        )
        response.raise_for_status()
        return self._parse_json(response)
