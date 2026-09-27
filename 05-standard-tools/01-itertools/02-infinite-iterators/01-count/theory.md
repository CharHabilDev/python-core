# count()

## What is `count()`?

`count()` creates an iterator that generates numbers indefinitely.

Each new value is produced only when requested.

---

## Syntax

```python
count(start=0, step=1)
```

Parameters:

| Parameter | Description              |
| --------- | ------------------------ |
| start     | First value              |
| step      | Increment between values |

Returns:

```text
Iterator
```

---

## Basic Example

```text
count(0)

0
1
2
3
4
...
```

---

## Starting Value

You can choose where counting begins.

```text
count(10)

10
11
12
13
14
...
```

---

## Step Value

You can specify the increment.

```text
count(0, 2)

0
2
4
6
8
...
```

---

## Negative Steps

Counting can go backwards.

```text
count(10, -1)

10
9
8
7
6
...
```

---

## Infinite Iterator

`count()` never stops by itself.

```text
count()
↓
0
1
2
3
4
...
∞
```

Because it is infinite, it is usually combined with tools that limit iteration.

---

## Lazy Evaluation

Values are generated only when requested.

```text
next()
↓
0

next()
↓
1

next()
↓
2
```

Nothing is created in advance.

---

## Memory Efficiency

This:

```text
count()
```

does not store millions of numbers.

Only the current state is kept in memory.

This makes it very efficient.

---

## Common Use Cases

### Generate IDs

```text
ID001
ID002
ID003
...
```

---

### Create Counters

```text
Visitor 1
Visitor 2
Visitor 3
...
```

---

### Numbering Data

```text
1. Alice
2. Thomas
3. Yasmine
```

---

### Simulations

```text
Turn 1
Turn 2
Turn 3
...
```

---

## count() vs range()

### range()

```text
Finite
```

Example:

```text
0
1
2
3
4
```

Stops automatically.

---

### count()

```text
Infinite
```

Example:

```text
0
1
2
3
4
...
```

Never stops.

---

## Key Takeaways

```text
count()
↓
infinite iterator
↓
lazy evaluation
↓
memory efficient
↓
start + step
```