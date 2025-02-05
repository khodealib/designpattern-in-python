# Singleton Pattern in Python

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This is
useful when exactly one object is needed to coordinate actions across the system.

## Implementation

Here is a simple implementation of the Singleton Pattern in Python:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
```

## Thread-Safe Implementation

To make the Singleton Pattern thread-safe, you can use a lock to ensure that only one thread can create the instance at
a time:

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
```

## Explanation

-   `__new__` method: This method is responsible for creating a new instance of the class. It is called before
    `__init__`.
-   `_instance` attribute: This class attribute holds the single instance of the class.
-   The `if not cls._instance` check ensures that only one instance of the class is created.
-   `_lock` attribute: This class attribute is a threading lock to ensure thread safety.

## Benefits

-   Controlled access to the sole instance.
-   Reduced namespace pollution.
-   Permits refinement of operations and representation.

## Drawbacks

-   Can be difficult to test due to global state.
-   May introduce hidden dependencies.

## Use Cases

-   Logger classes.
-   Configuration classes.
-   Access to resources that are shared (e.g., database connections).

## Conclusion

The Singleton Pattern is a powerful tool in software design, ensuring that a class has only one instance and providing a
global point of access to it. Use it wisely to manage shared resources and control access to critical sections of your
code.
