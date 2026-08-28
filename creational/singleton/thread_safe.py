"""Thread-safe Singleton implementation using metaclass."""

import threading
from typing import Any


class SingletonMeta(type):
    """Metaclass that ensures only one instance per class exists."""

    _instances: dict[type, Any] = {}
    _lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class ThreadSafeDatabaseConnection(metaclass=SingletonMeta):
    """Database connection singleton — URL set on first init only."""

    def __init__(self, database_url: str) -> None:
        self.database_url = database_url


def test_thread_safe(database_url: str) -> None:
    connection = ThreadSafeDatabaseConnection(database_url)
    print(connection.database_url)


if __name__ == "__main__":
    print("If you see the same value, singleton was reused (yay!)\nRESULT:")

    thread1 = threading.Thread(target=test_thread_safe, args=("FOO",))
    thread2 = threading.Thread(target=test_thread_safe, args=("BAR",))

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
