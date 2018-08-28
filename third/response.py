import requests


def http_response_status_code(url: str) -> int:
    """Return http response status code as an integer (e.g 200)."""

    return requests.get(url).status_code
