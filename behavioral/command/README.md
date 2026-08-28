# Command Pattern

Encapsulate a request as an object, thereby letting you parameterize clients with different requests.

## When to Use

- Parameterize objects by action to perform
- Queue, schedule, or execute requests at different times
- Support undo/redo
- Structure system around high-level operations (transactions)

## When to Avoid

- Simple callbacks — function/lambda is simpler
- Few commands — overkill
- Performance-critical hot path — command object adds overhead

## Run

```bash
python -m behavioral.command.command
```