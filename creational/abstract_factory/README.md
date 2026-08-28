# Abstract Factory Pattern

Provide an interface for creating families of related objects without specifying their concrete classes.

## When to Use

- System must work with multiple product families (e.g., UI themes, database drivers, cloud providers)
- Products in a family are designed to work together
- Want to enforce consistency across related objects
- Need to swap entire families at runtime

## When to Avoid

- Only one product family — no need for abstraction
- Families rarely change — YAGNI, use concrete factories directly
- Few products per family — simple factory or DI is simpler
- Adding new products requires changing all factories (OCP violation)

## Run

```bash
python -m creational.abstract_factory.abstract_factory
```