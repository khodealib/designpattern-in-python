"""Command pattern implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Receiver:
    def do_something(self, payload: str) -> None:
        print(f"Receiver: Working on ({payload})")

    def do_something_else(self, payload: str) -> None:
        print(f"Receiver: Also working on ({payload})")


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing ({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, payload_a: str, payload_b: str) -> None:
        self._receiver = receiver
        self._payload_a = payload_a
        self._payload_b = payload_b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object.")
        self._receiver.do_something(self._payload_a)
        self._receiver.do_something_else(self._payload_b)


class Invoker:
    def __init__(self) -> None:
        self._on_start: Command | None = None
        self._on_finish: Command | None = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if self._on_start:
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if self._on_finish:
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

    invoker.do_something_important()
