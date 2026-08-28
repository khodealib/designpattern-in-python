"""Non-thread-safe Singleton implementation using metaclass."""

from typing import Any


class SingletonMeta(type):
    """Metaclass that ensures only one instance per class exists (not thread-safe)."""

    _instances: dict[type, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """Simple logger singleton."""

    @staticmethod
    def log(msg: str) -> None:
        print(msg)


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Hello")
    logger2.log("World")

    print("Same instance?")
    print(logger1 is logger2)
