# Collections Cheat Sheet

Python's `collections` module provides specialized container data types.

---

# deque

Double-ended queue.

Useful for:

- FIFO queues
- LIFO stacks
- Rotations
- Recent history

## Import

```python
from collections import deque
```

## Create

```python
queue = deque()
queue = deque([1, 2, 3])
queue = deque(maxlen=5)
```

## Methods

### append()

Add to the right.

```python
queue.append("Task A")
```

Returns:

```python
None
```

---

### appendleft()

Add to the left.

```python
queue.appendleft("Task A")
```

Returns:

```python
None
```

---

### pop()

Remove from the right.

```python
item = queue.pop()
```

Returns:

```python
element
```

---

### popleft()

Remove from the left.

```python
item = queue.popleft()
```

Returns:

```python
element
```

---

### rotate()

Rotate elements.

```python
queue.rotate(1)
queue.rotate(-1)
```

Returns:

```python
None
```

---

## Common Uses

### FIFO Queue

```python
queue.append(task)
queue.popleft()
```

### Browser History (LIFO)

```python
history.append(page)
history.pop()
```

### Recent Searches

```python
searches = deque(maxlen=5)
```

---

# namedtuple

Tuple with named fields.

Useful for:

* Records
* Lightweight data structures

## Import

```python
from collections import namedtuple
```

## Create Type

```python
Person = namedtuple(
    "Person",
    ["name", "age", "country"]
)
```

Returns:

```python
new type
```

---

## Create Instance

```python
person = Person(
    "Alice",
    25,
    "Belgium"
)
```

Returns:

```python
Person object
```

---

## Access

### By Name

```python
person.name
person.age
```

### By Index

```python
person[0]
person[1]
```

---

## Special Methods

### _fields

Get field names.

```python
Person._fields
```

Returns:

```python
tuple
```

Example:

```python
('name', 'age', 'country')
```

---

### _asdict()

Convert to dictionary.

```python
person._asdict()
```

Returns:

```python
dict
```

---

### _replace()

Create modified copy.

```python
person._replace(age=26)
```

Returns:

```python
new namedtuple
```

---

### _make()

Create from iterable.

```python
Person._make(
    ["Alice", 25, "Belgium"]
)
```

Returns:

```python
Person object
```

---

## Common Uses

### Student Record

```python
Student(
    id,
    name,
    grade
)
```

### Product Catalog

```python
Product(
    name,
    price,
    stock
)
```

### Contact

```python
Contact(
    id,
    name,
    phone,
    email
)
```

---

# defaultdict

Dictionary with automatic default values.

Useful for:

* Grouping
* Counting
* Avoiding KeyError

## Import

```python
from collections import defaultdict
```

## Create

### List Default

```python
groups = defaultdict(list)
```

### Integer Default

```python
counter = defaultdict(int)
```

### Set Default

```python
items = defaultdict(set)
```

---

## Grouping Example

```python
groups = defaultdict(list)

groups["High"].append(
    "Fix login bug"
)
```

Result:

```python
{
    "High": [
        "Fix login bug"
    ]
}
```

---

## Counting Example

```python
counter = defaultdict(int)

counter["Python"] += 1
```

Result:

```python
{
    "Python": 1
}
```

---

## Common Uses

### Group Contacts by City

```python
cities[contact.city].append(
    contact.name
)
```

### Group Tasks by Priority

```python
tasks[task.priority].append(
    task.title
)
```

---

# Counter

Dictionary specialized for counting.

Useful for:

* Frequencies
* Statistics
* Rankings

## Import

```python
from collections import Counter
```

## Create

### From Iterable

```python
counter = Counter(
    ["python", "sql", "python"]
)
```

### From String

```python
counter = Counter(
    "hello"
)
```

### From List

```python
counter = Counter(words)
```

Returns:

```python
Counter object
```

---

## Methods

### most_common()

```python
counter.most_common()
```

Returns:

```python
list[tuple]
```

Example:

```python
[
    ("python", 10),
    ("sql", 5)
]
```

---

### most_common(n)

```python
counter.most_common(3)
```

Returns:

```python
top n elements
```

---

## Access Count

```python
counter["python"]
```

Returns:

```python
int
```

---

## Total Count

```python
sum(counter.values())
```

Returns:

```python
int
```

---

## Unique Elements

```python
len(counter)
```

Returns:

```python
int
```

---

## Common Uses

### Text Analyzer

```python
Counter(text.split())
```

### Contact Statistics

```python
Counter(cities)
```

### Task Statistics

```python
Counter(statuses)
Counter(priorities)
```

---

# Quick Summary

| Structure     | Main Purpose             |
| ------------- | ------------------------ |
| `deque`       | Queue / Stack            |
| `namedtuple`  | Lightweight record       |
| `defaultdict` | Automatic default values |
| `Counter`     | Counting frequencies     |