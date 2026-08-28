# Observer Pattern

Define a one-to-many dependency so that when one object changes state, all dependents are notified.

## When to Use

- Abstract model has two aspects, one dependent on the other
- Change to one object requires changing others, unknown count
- Object should notify others without knowing who they are

## When to Avoid

- Simple one-to-one — direct call is simpler
- High-frequency updates — observer overhead adds up
- Need guaranteed delivery/ordering — use message queue
- Memory leaks — observers must be detached (weakref helps)

## Run

```bash
python -m behavioral.observer.observer
```