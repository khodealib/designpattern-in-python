"""Adapter pattern implementation."""

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    print(target.request())


class ConcreteTarget(Target):
    def request(self) -> str:
        return "Target: The default target's behavior."


if __name__ == "__main__":
    print("Client: I can work just fine with Target objects:")
    target = ConcreteTarget()
    client_code(target)

    print("\nClient: The Adaptee class has a weird interface:")
    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.specific_request()}")

    print("\nClient: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
