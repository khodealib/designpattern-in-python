"""Prototype pattern implementation."""

from __future__ import annotations

import copy
from abc import ABC, abstractmethod
from typing import Any, cast


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Prototype:
        pass


class ConcretePrototype(Prototype):
    def __init__(self, name: str, data: dict[str, Any]) -> None:
        self.name = name
        self.data = data

    def clone(self) -> ConcretePrototype:
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"ConcretePrototype(name={self.name!r}, data={self.data})"


class PrototypeRegistry:
    def __init__(self) -> None:
        self._prototypes: dict[str, Prototype] = {}

    def register(self, name: str, prototype: Prototype) -> None:
        self._prototypes[name] = prototype

    def unregister(self, name: str) -> None:
        del self._prototypes[name]

    def clone(self, prototype_name: str, **attrs: Any) -> ConcretePrototype:
        prototype = self._prototypes[prototype_name]
        clone = cast(ConcretePrototype, prototype.clone())
        for key, value in attrs.items():
            setattr(clone, key, value)
        return clone


if __name__ == "__main__":
    registry = PrototypeRegistry()

    original = ConcretePrototype("template", {"tags": ["base"], "count": 0})
    registry.register("default", original)

    clone1 = registry.clone("default", name="clone1")
    clone1.data["tags"].append("modified")
    clone1.data["count"] = 1

    clone2 = registry.clone("default", name="clone2")
    clone2.data["count"] = 2

    print(f"Original: {original}")
    print(f"Clone 1:  {clone1}")
    print(f"Clone 2:  {clone2}")
    print(f"Original unchanged: {original.data}")
