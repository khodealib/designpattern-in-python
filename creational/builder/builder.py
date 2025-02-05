"""
This module demonstrates the Builder design pattern.
The Builder pattern is used to construct complex objects step by step. It allows for the creation of different representations of an object using the same construction process.
Classes:
    Product: Represents the complex object under construction.
    Builder: Abstract base class for building parts of the Product.
    ConcreteBuilder: Concrete implementation of the Builder interface.
    Director: Constructs the Product using a Builder instance.
Usage:
    The client creates a ConcreteBuilder and a Director. The Director is given the ConcreteBuilder and constructs the Product by calling the builder's methods. The final Product is then retrieved from the builder.

"""

from typing import List


class Product:
    def __init__(self) -> None:
        """Initialize the product with an empty list of parts."""
        self.parts: List[str] = []

    def add(self, part: str) -> None:
        """Add a part to the product.

        Args:
            part (str): The part to add to the product.
        """
        self.parts.append(part)

    def show(self) -> None:
        """Display the parts of the product."""
        print("Product parts: ", self.parts)


class Builder:
    def build_part_a(self) -> None:
        """Build part A of the product."""
        raise NotImplementedError

    def build_part_b(self) -> None:
        """Build part B of the product."""
        raise NotImplementedError

    def get_result(self) -> Product:
        """Get the final product.

        Returns:
            Product: The final product.
        """
        raise NotImplementedError


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        """Initialize the concrete builder with a new product."""
        self.product = Product()

    def build_part_a(self) -> None:
        """Build part A and add it to the product."""
        self.product.add("PartA")

    def build_part_b(self) -> None:
        """Build part B and add it to the product."""
        self.product.add("PartB")

    def get_result(self) -> Product:
        """Get the final product.

        Returns:
            Product: The final product.
        """
        return self.product


class Director:
    def __init__(self, builder: Builder) -> None:
        """Initialize the director with a builder.

        Args:
            builder (Builder): The builder to use for construction.
        """
        self.builder = builder

    def construct(self) -> None:
        """Construct the product using the builder."""
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    # Create a concrete builder
    builder = ConcreteBuilder()

    # Create a director with the builder
    director = Director(builder)

    # Construct the product
    director.construct()

    # Get the final product from the builder
    product = builder.get_result()

    # Show the product parts
    product.show()
