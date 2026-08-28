"""Classic Builder pattern implementation."""

from abc import ABC, abstractmethod


class Product:
    """The complex object being built."""

    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def show(self) -> None:
        print("Product parts:", self.parts)


class Builder(ABC):
    """Abstract builder interface."""

    @abstractmethod
    def build_part_a(self) -> None:
        pass

    @abstractmethod
    def build_part_b(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Product:
        pass


class ConcreteBuilder(Builder):
    """Concrete builder that constructs a specific Product."""

    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self) -> None:
        self.product.add("PartA")

    def build_part_b(self) -> None:
        self.product.add("PartB")

    def get_result(self) -> Product:
        return self.product


class Director:
    """Controls the construction process using a Builder."""

    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def construct(self) -> None:
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    product.show()
