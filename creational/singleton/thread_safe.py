"""
Singleton
    - Ensure that a class has only one instance and provide a global point of access to it.
    - Ensure that in each thread there is only one instance of the class.
"""

import threading


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible variations include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    we use a dictionary to keep track of the instances created, and a lock to synchronize access to the dictionary
    """

    _instance = None

    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class ThreadSafeDatabaseConnection(metaclass=SingletonMeta):
    """
    Used to connect to the database, and we prove with `database_url` parameter to be unchanged in multiple threads
    """

    database_url: str = None

    def __init__(self, database_url: str) -> None:
        self.database_url = database_url


def test_thread_safe(database_url: str) -> None:
    connection = ThreadSafeDatabaseConnection(database_url)
    print(connection.database_url)


if __name__ == "__main__":
    # The Client Code

    print("If you see the same value, then singleton was reused (yay!)\n" "RESULT:\n")

    thread1 = threading.Thread(target=test_thread_safe, args=("FOO",))
    thread2 = threading.Thread(target=test_thread_safe, args=("BAR",))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
