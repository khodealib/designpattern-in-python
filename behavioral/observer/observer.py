"""Observer pattern implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._state: int = 0

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state += 1
        print(f"Subject: My state has changed to {self._state}")
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if isinstance(subject, ConcreteSubject) and subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if isinstance(subject, ConcreteSubject) and subject._state >= 3:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()
