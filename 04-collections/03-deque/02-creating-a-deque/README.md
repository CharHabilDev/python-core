# Creating a Deque

## Summary

### Creation

A deque is created using the `deque()` constructor.

### Accepted Sources

- List
- Tuple
- String
- Range
- Other iterables

### Mental Model

```text
Iterable

↓

deque()

↓

Deque Object
```

## Examples

```python
deque(["apple", "banana"])

deque(("red", "blue"))

deque("hello")

deque(range(5))
```

## Key Idea

A deque can be created from any iterable object.