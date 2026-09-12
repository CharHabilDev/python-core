# Creating a namedtuple

## Summary

### Syntax

```python
namedtuple(type_name, field_names)
```

### Creation

```python
Person = namedtuple(
    "Person",
    ["name", "age", "country"]
)
```

### Instance

```python
person = Person(
    "Alice",
    25,
    "Belgium"
)
```

### Components

- Type name
- Field names
- Instances

### Typical Uses

- People
- Students
- Products
- Rabbits
- Coordinates

### Key Idea

```text
namedtuple()

↓

new type

↓

instances

↓

named fields
```