# Strategy Pattern

Define a family of algorithms, encapsulate each one, and make them interchangeable.

## When to Use

- Many related classes differ only in behavior
- Need different variants of an algorithm
- Algorithm uses data clients shouldn't know about
- Class defines many behaviors, conditional logic selects one

## When to Avoid

- Only one algorithm — no need for abstraction
- Algorithms rarely change — YAGNI
- Simple conditional (`if strategy == "a"`) is clearer
- Performance-critical — strategy call adds indirection

## Run

```bash
python -m behavioral.strategy.strategy
```