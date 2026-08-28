# Singleton Pattern

Ensure a class has only one instance and provide a global access point.

## When to Use

- Single shared resource (database connection pool, config, logger)
- Coordinating access across threads/processes
- Caching expensive-to-create objects

## When to Avoid

- Global state makes testing harder — inject the instance instead
- Multiple "singletons" needed (use a registry/factory instead)
- Stateless utilities — just use module-level functions

## Implementations

| File | Thread-Safe | Notes |
|------|-------------|-------|
| `thread_safe.py` | ✅ Yes | `threading.Lock` in metaclass `__call__` |
| `non_thread_safe.py` | ❌ No | Simpler, faster, single-threaded only |

## Run

```bash
python -m creational.singleton.thread_safe
python -m creational.singleton.non_thread_safe
```
