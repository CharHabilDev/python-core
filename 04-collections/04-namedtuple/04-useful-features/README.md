# Useful Features

## Built-in Features

A namedtuple provides useful methods and attributes.

These features make it easier to inspect, create, and modify data.

---

### _fields

Returns the field names.

```python
Person._fields
```

Result:

```python
('name', 'age', 'country')
```

---

### _asdict()

Converts a namedtuple into a dictionary.

```python
person._asdict()
```

Result:

```python
{
    'name': 'Alice',
    'age': 25,
    'country': 'Belgium'
}
```

---

### _replace()

Creates a new instance with modified values.

```python
person._replace(age=30)
```

Result:

```python
Person(
    name='Alice',
    age=30,
    country='Belgium'
)
```

The original object is not modified.

---

## Why _replace()?

namedtuple objects are immutable.

This is not allowed:

```python
person.age = 30
```

Instead:

```python
person = person._replace(age=30)
```

---

### _make()

Creates an instance from an iterable.

```python
data = ["Alice", 25, "Belgium"]

person = Person._make(data)
```

Result:

```python
Person(
    name='Alice',
    age=25,
    country='Belgium'
)
```

---

### _## Key Idea

```text
_fields
↓
inspect

_asdict()
↓
convert

_replace()
↓
copy

_make()
↓
create
```