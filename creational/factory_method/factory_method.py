"""Factory Method pattern implementation."""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    msg = "Client: I'm not aware of the creator's class, but it still works."
    print(f"{msg}\n{creator.some_operation()}")


if __name__ == "__main__":
    print("App: Launched with ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\nApp: Launched with ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
