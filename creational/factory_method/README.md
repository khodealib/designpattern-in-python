# Factory Method Pattern

Define an interface for creating an object, but let subclasses decide which class to instantiate.

## When to Use

- Class can't anticipate the class of objects it must create
- Class wants its subclasses to specify the objects it creates
- Delegating responsibility to one of several helper subclasses

## When to Avoid

- Only one product type — no need for abstraction
- Tight coupling to concrete classes is acceptable
- Simple instantiation logic — `if/elif` or dict lookup is simpler

## Run

```bash
python -m creational.factory_method.factory_method
```