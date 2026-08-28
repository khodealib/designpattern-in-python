"""Abstract Factory pattern implementation."""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self) -> str:
        return "Result of ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self) -> str:
        return "Result of ConcreteProductA2"


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str:
        pass


class ConcreteProductB1(AbstractProductB):
    def operation_b(self) -> str:
        return "Result of ConcreteProductB1"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self) -> str:
        return "Result of ConcreteProductB2"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.operation_a())
    print(product_b.operation_b())


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\nClient: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
