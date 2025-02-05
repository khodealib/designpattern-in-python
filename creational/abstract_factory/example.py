from abc import ABC, abstractmethod

# Abstract Product A
class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass

    @abstractmethod
    def sit_on(self) -> str:
        pass

# Concrete Product A1
class VictorianChair(Chair):
    def has_legs(self) -> str:
        return "Victorian Chair has 4 legs."

    def sit_on(self) -> str:
        return "Sitting on a Victorian Chair."

# Concrete Product A2
class ModernChair(Chair):
    def has_legs(self) -> str:
        return "Modern Chair has 4 legs."

    def sit_on(self) -> str:
        return "Sitting on a Modern Chair."

# Abstract Product B
class Sofa(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass

    @abstractmethod
    def lie_on(self) -> str:
        pass

# Concrete Product B1
class VictorianSofa(Sofa):
    def has_legs(self) -> str:
        return "Victorian Sofa has 4 legs."

    def lie_on(self) -> str:
        return "Lying on a Victorian Sofa."

# Concrete Product B2
class ModernSofa(Sofa):
    def has_legs(self) -> str:
        return "Modern Sofa has 4 legs."

    def lie_on(self) -> str:
        return "Lying on a Modern Sofa."

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# Concrete Factory 1
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

# Concrete Factory 2
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

# Client code
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