from lord_rings_sdk.movie import (
    Movie,
)
from typing import (
    Literal,
)


class Client(object):
    """
    A client for the lord of the rings API.
    """

    def __init__(
        self, env: Literal["dev"] = "dev", version: Literal["v2"] = "v2"
    ):
        self.env = env
        self.version = version
        base_url = {"dev": "https://the-one-api.dev"}
        try:
            self.base_url = base_url[self.env]
        except AttributeError:
            raise Exception("The environment is invalid")

        # resources
        self.movie = Movie(self.base_url, "movie", self.version)
