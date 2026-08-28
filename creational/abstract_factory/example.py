"""Abstract Factory pattern - Furniture example."""

from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass

    @abstractmethod
    def sit_on(self) -> str:
        pass


class VictorianChair(Chair):
    def has_legs(self) -> str:
        return "Victorian Chair has 4 legs."

    def sit_on(self) -> str:
        return "Sitting on a Victorian Chair."


class ModernChair(Chair):
    def has_legs(self) -> str:
        return "Modern Chair has 4 legs."

    def sit_on(self) -> str:
        return "Sitting on a Modern Chair."


class Sofa(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass

    @abstractmethod
    def lie_on(self) -> str:
        pass


class VictorianSofa(Sofa):
    def has_legs(self) -> str:
        return "Victorian Sofa has 4 legs."

    def lie_on(self) -> str:
        return "Lying on a Victorian Sofa."


class ModernSofa(Sofa):
    def has_legs(self) -> str:
        return "Modern Sofa has 4 legs."

    def lie_on(self) -> str:
        return "Lying on a Modern Sofa."


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


def client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.has_legs())
    print(chair.sit_on())
    print(sofa.has_legs())
    print(sofa.lie_on())


if __name__ == "__main__":
    print("Client: Testing client code with the Victorian furniture factory:")
    client_code(VictorianFurnitureFactory())

    print("\nClient: Testing the same client code with the Modern furniture factory:")
    client_code(ModernFurnitureFactory())
