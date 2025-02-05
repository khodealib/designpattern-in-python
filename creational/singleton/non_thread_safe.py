"""
Singleton:
    - Ensure that a class has only one instance and provide a global point of access to it.
    - Thread unsafe
"""


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible variations include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance = None

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not
        affect the returned instance.
        """
        if cls not in cls._instances:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=SingletonMeta):
    @staticmethod
    def log(msg):
        print(msg)


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Hello")
    logger2.log("World")

    print("That's the same instance?")
    print(logger1 is logger2)
