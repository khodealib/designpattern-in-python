"""Strategy pattern implementation."""

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data: list[int]) -> list[int]:
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)


class ConcreteStrategyC(Strategy):
    def execute(self, data: list[int]) -> list[int]:
        return [x for x in data if x % 2 == 0]


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self, data: list[int]) -> list[int]:
        print(f"Context: Sorting data using {self._strategy.__class__.__name__}")
        return self._strategy.execute(data)


if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    context = Context(ConcreteStrategyA())
    print(f"Result: {context.do_some_business_logic(data)}")
    print()

    context.strategy = ConcreteStrategyB()
    print(f"Result: {context.do_some_business_logic(data)}")
    print()

    context.strategy = ConcreteStrategyC()
    print(f"Result: {context.do_some_business_logic(data)}")
