# Design Patterns in Python

Executable reference implementations of design patterns in modern, typed Python. Not diagrams — runnable code showing how patterns map to Python 3.11+ language features.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/mypy-strict-brightgreen)](https://mypy-lang.org/)
[![Patterns](https://img.shields.io/badge/patterns-11%20implemented-orange)]()

## Table of Contents

### Creational Patterns

1. [Singleton](./creational/singleton/) — Ensure one instance, global access
2. [Builder](./creational/builder/) — Step-by-step construction of complex objects
3. [Abstract Factory](./creational/abstract_factory/) — Families of related objects
4. [Factory Method](./creational/factory_method/) — Delegate instantiation to subclasses
5. [Prototype](./creational/prototype/) — Clone existing instances

### Structural Patterns

6. [Adapter](./structural/adapter/) — Bridge incompatible interfaces
7. [Decorator](./structural/decorator/) — Add responsibilities dynamically
8. [Facade](./structural/facade/) — Simplify subsystem interface

### Behavioral Patterns

9. [Strategy](./behavioral/strategy/) — Interchangeable algorithms
10. [Observer](./behavioral/observer/) — Publish-subscribe notifications
11. [Command](./behavioral/command/) — Encapsulate requests as objects

## Quick Start

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run a pattern
python -m creational.singleton.thread_safe
python -m creational.builder.builder
python -m creational.abstract_factory.abstract_factory
python -m creational.factory_method.factory_method
python -m creational.prototype.prototype
python -m structural.adapter.adapter
python -m structural.decorator.decorator
python -m structural.facade.facade
python -m behavioral.strategy.strategy
python -m behavioral.observer.observer
python -m behavioral.command.command

# Lint & type-check
ruff check .
mypy .
```

## Pattern Quality Checklist

Each implemented pattern includes:
- ✅ Full type hints (mypy strict)
- ✅ Runnable example in `__main__`
- ✅ README with "When to use / Avoid" guidance
- ✅ Ruff-formatted, mypy-clean code

## Contributing

Contributions welcome! Please:
1. Add type hints (mypy strict)
2. Include a runnable `__main__` demo
3. Add a pattern README with "When to use / Avoid"
4. Run `ruff check --fix . && mypy .` before PR

## License

MIT License — see [LICENSE](./LICENSE)

## Sources

- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Wikipedia](https://en.wikipedia.org/wiki/Software_design_pattern)
- [SourceMaking](https://sourcemaking.com/design_patterns)