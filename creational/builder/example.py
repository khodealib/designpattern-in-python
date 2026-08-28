"""Fluent Builder pattern for HTTP requests."""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class Request:
    method: str
    endpoint: str
    headers: dict[str, str]
    payload: dict[str, str]


class RequestBuilder:
    """Fluent builder for Request objects."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._method: str | None = None
        self._endpoint: str | None = None
        self._headers: dict[str, str] = {}
        self._payload: dict[str, str] = {}

    def set_method(self, method: str | None = None) -> RequestBuilder:
        self._method = method or "GET"
        return self

    def set_endpoint(self, endpoint: str) -> RequestBuilder:
        self._endpoint = endpoint
        return self

    def set_headers(self, headers: dict[str, str]) -> RequestBuilder:
        self._headers.update(headers)
        return self

    def set_payload(self, payload: dict[str, str]) -> RequestBuilder:
        self._payload.update(payload)
        return self

    def build(self) -> Request:
        if not self._endpoint:
            raise ValueError("Endpoint must be set before building the request.")
        request = Request(
            method=self._method or "GET",
            endpoint=self._endpoint,
            headers=self._headers,
            payload=self._payload,
        )
        self.reset()
        return request


class Director:
    """Convenience methods for common request types."""

    def __init__(self, builder: RequestBuilder) -> None:
        self._builder = builder

    def get_request(self, endpoint: str) -> Request:
        return self._builder.set_method("GET").set_endpoint(endpoint).build()

    def post_request(
        self,
        endpoint: str,
        headers: dict[str, str],
        payload: dict[str, str],
    ) -> Request:
        return (
            self._builder.set_method("POST")
            .set_endpoint(endpoint)
            .set_headers(headers)
            .set_payload(payload)
            .build()
        )


if __name__ == "__main__":
    builder = RequestBuilder()
    director = Director(builder)

    req1 = director.get_request("http://google.com")
    req2 = director.post_request(
        "http://api.example.com/resource",
        {"Content-Type": "application/json", "Authorization": "Bearer token"},
        {"foo": "bar", "baz": "qux"},
    )

    print(req1)
    print(req2)
