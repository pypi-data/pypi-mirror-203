from lord_rings_sdk.types import (
    Parameters,
)
from lord_rings_sdk.utils import (
    request,
)
from typing import (
    Any,
)


class Movie:
    def __init__(self, base_url: str, resource: str, version: str) -> None:
        """
        Initialize the Movie resource
        """
        super(Movie, self)
        self.base_url = base_url
        self.resource = resource
        self.version = version

    def get(
        self,
        id: str | None = None,
        parameters: Parameters | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        return request(
            self.base_url,
            self.resource,
            self.version,
            id=id,
            parameters=parameters,
            headers=headers,
        )

    def get_quote(
        self,
        id: str,
        parameters: Parameters | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        return request(
            self.base_url,
            self.resource,
            self.version,
            id=id,
            parameters=parameters,
            headers=headers,
            relations=[("quote", None)],
        )
