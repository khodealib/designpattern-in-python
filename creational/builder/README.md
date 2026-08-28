# Builder Pattern

Separate construction of a complex object from its representation.

## When to Use

- Object has many optional/configurable parameters
- Construction involves multiple steps that must be ordered
- Need different representations from same construction process
- Immutable objects with many fields (fluent builder)

## When to Avoid

- Simple objects with few required fields — just use `__init__` or dataclass
- Single representation, no step-by-step logic — factory is simpler
- Performance-critical hot paths — builder adds indirection

## Implementations

| File | Style | Best For |
|------|-------|----------|
| `builder.py` | Classic GoF (Director + Abstract Builder) | Multiple product types, same construction algorithm |
| `example.py` | Fluent Builder (method chaining) | Single product, many optional fields, readable DSL |

## Run

```bash
python -m creational.builder.builder
python -m creational.builder.example
```
