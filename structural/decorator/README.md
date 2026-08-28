# Decorator Pattern

Attach additional responsibilities to an object dynamically.

## When to Use

- Add responsibilities to individual objects without affecting others
- Withdraw responsibilities (via removal)
- Extension by subclassing is impractical (many independent extensions)
- Runtime composition of behaviors

## When to Avoid

- Simple cases — just use composition or inheritance directly
- Many decorators cause complexity (debugging, stack traces)
- All objects need same behavior — inherit or compose once

## Run

```bash
python -m structural.decorator.decorator
```