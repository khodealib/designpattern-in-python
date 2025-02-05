"""
Builder Pattern:
    The Builder Pattern is a creational design pattern used to construct objects step by step.
    Its main purpose is to enable the creation of objects with multiple customizable options
    during the construction process. This pattern provides greater control and flexibility
    when building objects, especially those with optional or configurable parts.
    Use it when you need to create complex objects that require step-by-step assembly
    or involve optional configurations.

Main Difference with Factory Pattern:
    The main goal of the Factory Pattern is to create objects while hiding the complexity
    of the creation process. It is suitable when object creation does not need to be customizable.
"""

import dataclasses
from typing import Dict, Optional


@dataclasses.dataclass
class Request:
    method: str
    endpoint: str
    headers: Dict[str, str]
    payload: Dict[str, str]


class RequestBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._method: Optional[str] = None
        self._endpoint: Optional[str] = None
        self._headers: Dict[str, str] = {}
        self._payload: Dict[str, str] = {}

    def set_method(self, method: Optional[str] = None):
        """Set the HTTP method. Defaults to 'GET' if no method is provided."""
        self._method = method or "GET"
        return self

    def set_endpoint(self, endpoint: str):
        """Set the API endpoint."""
        self._endpoint = endpoint
        return self

    def set_headers(self, headers: Dict[str, str]):
        """Set or update headers."""
        self._headers.update(headers)
        return self

    def set_payload(self, payload: Dict[str, str]):
        """Set or update the payload."""
        self._payload.update(payload)
        return self

    def build(self) -> Request:
        """Build and return the Request object."""
        if not self._endpoint:
            raise ValueError("Endpoint must be set before building the request.")
        request = Request(
            method=self._method,
            endpoint=self._endpoint,
            headers=self._headers,
            payload=self._payload,
        )
        self.reset()  # Reset the builder for the next build
        return request


class Director:
    def __init__(self, builder: RequestBuilder):
        self._builder = builder

    def get_request(self, endpoint: str) -> Request:
        return self._builder.set_method("GET").set_endpoint(endpoint).build()

    def post_request(self, endpoint: str, headers: Dict[str, str], payload: Dict[str, str]) -> Request:
        return self._builder.set_method("POST").set_endpoint(endpoint).set_headers(headers).set_payload(payload).build()


if __name__ == "__main__":
    builder = RequestBuilder()
    director = Director(builder)

    # Example 1: GET request
    req1 = director.get_request("http://google.com")

    # Example 2: POST request with headers and payload
    req2 = director.post_request(
        "http://api.example.com/resource",
        {"Content-Type": "application/json", "Authorization": "Bearer token"},
        {"foo": "bar", "baz": "qux"},
    )

    print(req1)
    print(req2)
