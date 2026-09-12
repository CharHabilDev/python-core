# Real-World Use Cases

## When to Use namedtuple

A namedtuple is useful when:

- Data has a fixed structure.
- Values should not change.
- Readability is important.
- A full class would be unnecessary.

---

## Person Records

```text
Person

↓

name
age
country
```

Example uses:

- Employees
- Customers
- Users

---

## Product Catalog

```text
Product

↓

name
price
stock
```

Example uses:

- E-commerce
- Inventory systems
- Shop management

---

## Student Records

```text
Student

↓

name
classroom
grade
```

Example uses:

- School management
- Attendance systems
- Exam results

---

## Coordinates

```text
Coordinate

↓

latitude
longitude
```

Example uses:

- GPS applications
- Maps
- Delivery systems

---

## Rabbit Manager

```text
Rabbit

↓

id
name
breed
gender
```

Possible uses:

- Rabbit registry
- Statistics
- Reporting

---

## Medika

```text
Medicine

↓

name
price
stock
```

Possible uses:

- Pharmacy inventory
- Medicine search
- Stock monitoring

---

## Why Not a Dictionary?

Dictionary:

```python
rabbit["breed"]
```

namedtuple:

```python
rabbit.breed
```

The second is often easier to read.

---

## Why Not a Class?

If you only need to store data:

```text
namedtuple

↓

simple

↓

lightweight
```

A full class may be unnecessary.

---

## When Not to Use namedtuple

Avoid namedtuple when:

- Data changes frequently.
- Many methods are needed.
- Complex behavior is required.

In those cases, a class is usually better.

---

## Summary

### Good Choices

- Person
- Product
- Student
- Coordinate
- Rabbit
- Medicine

### Benefits

- Readable
- Lightweight
- Immutable

### Key Idea

```text
Fixed data

↓

namedtuple

↓

simple and readable
```