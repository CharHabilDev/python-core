# Introduction

## Summary

### namedtuple

A `namedtuple` is a tuple whose values can be accessed using names.

### Benefits

- Better readability
- Access by field name
- Lightweight structure
- Immutable data

### Comparison

```text
tuple

↓

person[0]
person[1]
person[2]
```

```text
namedtuple

↓

person.name
person.age
person.country
```

### Characteristics

- Ordered
- Immutable
- Access by index
- Access by name

### Common Use Cases

- People
- Students
- Products
- Coordinates
- Database records