"""Facade pattern implementation."""



class SubsystemA:
    def operation_a(self) -> str:
        return "SubsystemA: Ready!"

    def operation_b(self) -> str:
        return "SubsystemB: Go!"


class SubsystemB:
    def operation_c(self) -> str:
        return "SubsystemB: Set!"

    def operation_d(self) -> str:
        return "SubsystemB: Done!"


class SubsystemC:
    def operation_e(self) -> str:
        return "SubsystemC: Cleanup!"


class Facade:
    def __init__(self) -> None:
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation_1(self) -> list[str]:
        results = [
            self._subsystem_a.operation_a(),
            self._subsystem_b.operation_c(),
            self._subsystem_c.operation_e(),
        ]
        return results

    def operation_2(self) -> list[str]:
        results = [
            self._subsystem_b.operation_d(),
            self._subsystem_a.operation_b(),
        ]
        return results


def client_code(facade: Facade) -> None:
    print("Client: Operation 1")
    for result in facade.operation_1():
        print(f"  {result}")

    print("\nClient: Operation 2")
    for result in facade.operation_2():
        print(f"  {result}")


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
