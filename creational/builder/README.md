# Builder Pattern in Python

The Builder Pattern is a creational design pattern that allows for the step-by-step creation of complex objects. It separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

## Structure

1. **Builder**: Specifies an abstract interface for creating parts of a Product object.
2. **ConcreteBuilder**: Constructs and assembles parts of the product by implementing the Builder interface. It defines and keeps track of the representation it creates and provides an interface for retrieving the product.
3. **Director**: Constructs an object using the Builder interface.
4. **Product**: Represents the complex object under construction.

## Example

Here is an example of the Builder Pattern in Python:

```python
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product Parts: ", self.parts)

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA")

    def build_part_b(self):
        self.product.add("PartB")

    def get_result(self):
        return self.product

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

# Usage
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_result()
product.show()
```

## Advantages

- **Separation of Concerns**: The pattern separates the construction of a complex object from its representation.
- **Flexibility**: It allows for different representations of a constructed object.
- **Reusability**: The same construction process can be reused to create different products.

## Use Cases

- When the construction process of an object is complex.
- When you need to create different representations of a product.
- When the construction algorithm should be independent of the parts that make up the object and how they are assembled.

## References

- [Builder Pattern - Wikipedia](https://en.wikipedia.org/wiki/Builder_pattern)
- [Builder Pattern - Refactoring Guru](https://refactoring.guru/design-patterns/builder)
