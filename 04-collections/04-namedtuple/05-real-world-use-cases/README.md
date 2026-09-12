# Real-World Use Cases

## Summary

### Good Use Cases

- Person records
- Product catalogs
- Student records
- Coordinates
- Rabbit data
- Medicine data

### Why Use It?

- Readable field names
- Lightweight structure
- Immutable data

### Compared to Dictionaries

```python
person["name"]
```

↓

```python
person.name
```

### Compared to Classes

Use namedtuple when:

- Data is simple
- Structure is fixed
- No complex behavior is needed

### Key Idea

```text
Fixed data

↓

namedtuple

↓

simple and readable
```