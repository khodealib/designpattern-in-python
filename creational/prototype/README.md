# Prototype Pattern

Create new objects by copying an existing prototype instance.

## When to Use

- Object creation is expensive (complex initialization, DB queries, network calls)
- System should be independent of how its products are created/composed
- Classes to instantiate are specified at runtime
- Avoid building a class hierarchy of factories that parallels product hierarchy

## When to Avoid

- Simple objects — copying overhead not worth it
- Objects with circular references (need careful deepcopy handling)
- Shallow copy suffices — just use `copy.copy()` directly
- Immutables — just share the same instance

## Run

```bash
python -m creational.prototype.prototype
```