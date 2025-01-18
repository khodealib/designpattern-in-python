from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    Attributes:
        name (str): The name of the animal.
    """

    @abstractmethod
    def __init__(self, name):
        """
        Initialize the Animal with a name.

        Args:
            name (str): The name of the animal.
        """
        self.name = name


class Dog(Animal):
    """
    A concrete implementation of an Animal representing a dog.
    """

    def __init__(self, name):
        """
        Initialize the Dog with a name.

        Args:
            name (str): The name of the dog.
        """
        super().__init__(name)


class Cat(Animal):
    """
    A concrete implementation of an Animal representing a cat.
    """

    def __init__(self, name):
        """
        Initialize the Cat with a name.

        Args:
            name (str): The name of the cat.
        """
        super().__init__(name)


class AnimalFactory:
    """
    Factory class for creating Animal instances.

    This class uses a registry to store mappings between animal types and their respective classes.
    """

    _registry = {}

    @classmethod
    def register(cls, animal_type, animal_class):
        """
        Register an animal type with its corresponding class.

        Args:
            animal_type (str): The type of the animal (e.g., 'dog', 'cat').
            animal_class (type): The class corresponding to the animal type.

        Raises:
            ValueError: If the animal_class is not a subclass of Animal.
        """
        if not issubclass(animal_class, Animal):
            raise ValueError(f"{animal_class} is not a subclass of {Animal}")
        cls._registry[animal_type.lower()] = animal_class

    @classmethod
    def create_animal(cls, animal_type, name):
        """
        Create an instance of an Animal based on its type and name.

        Args:
            animal_type (str): The type of the animal (e.g., 'dog', 'cat').
            name (str): The name of the animal.

        Returns:
            Animal: An instance of the requested animal type.

        Raises:
            NotImplementedError: If the animal type is not registered in the factory.
        """
        animal_class = cls._registry.get(animal_type.lower())
        if not animal_class:
            raise NotImplementedError(f"{animal_class} not registered")
        return animal_class(name)


# Register Dog and Cat types in the AnimalFactory.
AnimalFactory.register('dog', Dog)
AnimalFactory.register('cat', Cat)

if __name__ == '__main__':
    # Create instances of Dog and Cat using the factory.
    dog = AnimalFactory.create_animal('dog', "John")
    cat = AnimalFactory.create_animal('cat', "Mosh")

    # Print the names of the created animals.
    print(dog.name)
    print(cat.name)