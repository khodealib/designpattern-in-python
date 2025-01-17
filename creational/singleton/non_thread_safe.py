"""
    Singleton:
        - Ensure that a class has only one instance and provide a global point of access to it.
        - Thread unsafe
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
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
