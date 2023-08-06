from os import (
    environ,
)
import requests
from lord_rings_sdk.types import (
    Parameters,
)
from typing import (
    Any,
)
from urllib.parse import (
    urlencode,
)


def _add_parameters(url: str, parameters: Parameters | None) -> str:
    """
    Add parameters for paginating, filtering and sorting
    """
    if not parameters:
        return url
    api_parameters = []
    if parameters.pagination:
        if parameters.pagination.limit:
            api_parameters.append(("limit", str(parameters.pagination.limit)))
        if parameters.pagination.page:
            api_parameters.append(("page", str(parameters.pagination.page)))
        if parameters.pagination.offset:
            api_parameters.append(("offset", str(parameters.pagination.offset)))

    if parameters.sorting:
        api_parameters.append(
            ("sort", f"{parameters.sorting.parameter}:{parameters.sorting.direction}")
        )

    if parameters.filtering:
        if parameters.filtering.matches:
            for match in parameters.filtering.matches:
                api_parameters.append((match.parameter, match.value))
        if parameters.filtering.not_matches:
            for match in parameters.filtering.not_matches:
                api_parameters.append((f"{match.parameter}!", match.value))

    if api_parameters:
        query_string = urlencode(api_parameters)
    return f"{url}?{query_string}"


def _build_path(
    base_url: str | None = None,
    resource: str | None = None,
    version: str | None = None,
    id: str | None = None,
    parameters: Parameters | None = None,
    relations: list[tuple[str, str | None]] = [],
) -> tuple[str, str]:
    paths = {
        "resources": {"movie": {"path": f"{version}/movie", "name": None}}
    }
    resource_info = paths["resources"][resource]
    sections = [resource_info["path"]]
    if id:
        sections.append(id)
    if relations:
        for resource, resource_id in relations:
            sections.append(resource)
            if resource_id:
                sections.append(resource_id)

    path = f'/{"/".join(sections)}'
    url = _add_parameters(f"{base_url}{path}", parameters)
    return [path, url]


def request(
    base_url: str,
    resource: str,
    version: str,
    id: str | None = None,
    parameters: Parameters | None = None,
    headers: dict[str, str] | None = None,
    relations: list[tuple[str, str | None]] = [],
) -> dict[str, Any]:
    headers = headers or {}
    if not headers.get("Authorization"):
        auth_token = environ.get("LORD_RINGS_TOKEN", "0X0LCPzgFem7mTKmrIxk")
        headers["Authorization"] = f"Bearer {auth_token}"
    _, url = _build_path(
        base_url=base_url,
        resource=resource,
        version=version,
        id=id,
        parameters=parameters,
        relations=relations,
    )
    response = requests.get(url, headers=headers)
    json_response: dict[str, Any] = response.json()
    return {"status": response.status_code, "json": json_response}
