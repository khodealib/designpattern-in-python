from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalFactory:
    _registry = {}

    @classmethod
    def register(cls, animal_type, animal_class):
        if not issubclass(animal_class, Animal):
            raise ValueError(f"{animal_class} is not a subclass of {Animal}")
        cls._registry[animal_type.lower()] = animal_class

    @classmethod
    def create_animal(cls, animal_type, name):
        animal_class = cls._registry.get(animal_type.lower())
        if not animal_class:
            raise NotImplementedError(f"{animal_class} not registered")
        return animal_class(name)


AnimalFactory.register('dog', Dog)
AnimalFactory.register('cat', Cat)

if __name__ == '__main__':
    dog = AnimalFactory.create_animal('dog', "John")
    cat = AnimalFactory.create_animal('cat', "Mosh")

    print(dog.name)
    print(cat.name)
