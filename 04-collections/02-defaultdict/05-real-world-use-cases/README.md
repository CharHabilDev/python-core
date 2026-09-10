# Real-World Use Cases

`defaultdict` is particularly useful when data must be counted, grouped, or organized automatically.

It reduces boilerplate code and avoids manual key initialization.

## Learning Objectives

After completing this chapter, I should be able to:

- Identify situations where `defaultdict` is useful.
- Choose the appropriate factory (`int`, `list`, `set`).
- Apply `defaultdict` to real-world problems.
- Group and organize data efficiently.
- Use `defaultdict` in personal projects.

---

## Common Use Cases

### Text Analysis

Count word frequencies using:

```python
defaultdict(int)
```

### Expense Tracking

Group expenses by category using:

```python
defaultdict(list)
```

### Event Management

Group events by month using:

```python
defaultdict(list)
```

### Rabbit Management

Group rabbits by breed using:

```python
defaultdict(list)
```

### Tag Systems

Store unique tags using:

```python
defaultdict(set)
```

---

## Factory Selection

| Need                | Factory |
| ------------------- | ------- |
| Count occurrences   | `int`   |
| Group values        | `list`  |
| Store unique values | `set`   |

---

## Key Idea

```text
Need to count?
↓
defaultdict(int)

Need multiple values?
↓
defaultdict(list)

Need unique values?
↓
defaultdict(set)
```