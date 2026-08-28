# Adapter Pattern

Allow incompatible interfaces to work together.

## When to Use

- Integrate a class with an incompatible interface
- Create a reusable class that cooperates with unrelated/unforeseen classes
- Use existing subclass but can't adapt interface by subclassing

## When to Avoid

- Both interfaces are under your control — change one to match
- Simple one-off conversion — inline adapter function is simpler
- Performance-critical hot path — adapter adds indirection

## Run

```bash
python -m structural.adapter.adapter
```