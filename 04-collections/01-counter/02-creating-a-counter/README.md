# Creating a Counter

## Summary

### Creating a Counter

A Counter can be created from any iterable.

Common sources include:

- Lists
- Strings
- Tuples

### Import

```python
from collections import Counter
```

### Examples

```python
Counter(["apple", "banana", "apple"])
```

```python
Counter("hello")
```

```python
Counter(("red", "blue", "red"))
```

### Key Idea

```text
Iterable
↓
Counter
↓
Occurrences
```

### Common Use Cases

- Text analysis
- Vote counting
- Log analysis
- Category statistics