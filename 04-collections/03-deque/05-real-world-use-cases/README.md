# Real-World Use Cases

## Summary

### Queue (FIFO)

```text
First In
↓
First Out
```

Examples:

- Print queue
- Customer queue
- Message queue

---

### Stack (LIFO)

```text
Last In
↓
First Out
```

Examples:

- Undo/Redo
- Browser history
- Call stack

---

### Recent History

Using:

```python
deque(maxlen=n)
```

Examples:

- Recent searches
- Notifications
- Recent files

---

### Circular Systems

Using:

```python
rotate()
```

Examples:

- Round-robin scheduling
- Turn-based games
- Team rotation

---

### Key Idea

A deque is useful whenever data must be added, removed, rotated, or limited efficiently.