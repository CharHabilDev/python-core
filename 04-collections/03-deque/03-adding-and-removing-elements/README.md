# Adding and Removing Elements

## Summary

### Adding Elements

```python
append()
appendleft()
```

- `append()` adds an element to the right.
- `appendleft()` adds an element to the left.

---

### Removing Elements

```python
pop()
popleft()
```

- `pop()` removes an element from the right.
- `popleft()` removes an element from the left.

---

### Mental Model

```text
appendleft()

↓

[A] [B] [C]

↑

popleft()
```

```text
append()

↓

[A] [B] [C]

↑

pop()
```

---

### FIFO

```text
First In
↓

First Out
```

Typical use cases:

- Print queue
- Customer queue
- Message queue

---

### LIFO

```text
Last In
↓

First Out
```

Typical use cases:

- Undo/Redo
- Browser history
- Stack processing

---

### Why deque?

Unlike a list, a deque is optimized for adding and removing elements at both ends.

### Key Methods

```python
append()
appendleft()

pop()
popleft()
```