# Facade Pattern

Provide a unified interface to a set of interfaces in a subsystem.

## When to Use

- Simplify complex subsystem interface
- Decouple clients from subsystem components
- Layer subsystems (entry point per layer)

## When to Avoid

- Subsystem is simple — direct access is fine
- Clients need fine-grained control over subsystem
- Subsystem changes frequently — facade becomes maintenance burden

## Run

```bash
python -m structural.facade.facade
```