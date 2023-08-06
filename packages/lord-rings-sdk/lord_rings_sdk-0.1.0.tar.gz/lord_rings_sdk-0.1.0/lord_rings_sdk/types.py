from typing import (
    Literal,
    NamedTuple,
)


class PaginationOptions(NamedTuple):
    limit: int | None = None
    page: int | None = None
    offset: int | None = None


class SortingOptions(NamedTuple):
    parameter: str
    direction: Literal["asc"]


class SortingOptions(NamedTuple):
    parameter: str
    direction: Literal["asc", "desc"]


class Match(NamedTuple):
    parameter: str
    value: str


class FilteringOptions(NamedTuple):
    matches: set[Match] | None = None
    not_matches: set[Match] | None = None


class Parameters(NamedTuple):
    pagination: PaginationOptions | None = None
    sorting: SortingOptions | None = None
    filtering: FilteringOptions | None = None
