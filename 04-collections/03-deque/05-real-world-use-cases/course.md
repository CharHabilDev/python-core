# Real-World Use Cases

## Why Use deque?

A deque is designed for efficient operations on both ends.

It is useful when elements are frequently added or removed from the beginning and the end of a collection.

---

## Queues (FIFO)

FIFO means:

```text
First In
↓
First Out
```

Typical examples:

- Print queues
- Customer service queues
- Message processing
- Task scheduling

Example:

```text
A enters
B enters
C enters

↓

A leaves
B leaves
C leaves
```

---

## Stacks (LIFO)

LIFO means:

```text
Last In
↓
First Out
```

Typical examples:

- Undo systems
- Browser navigation
- Function call stacks
- History systems

Example:

```text
A
B
C

↓

C leaves
B leaves
A leaves
```

---

## Recent History

Using `maxlen`, a deque can keep only the most recent items.

Examples:

- Search history
- Notifications
- Recent files
- Recent commands

Example:

```python
deque(maxlen=10)
```

Only the 10 most recent items are kept.

---

## Circular Processing

Using `rotate()`, a deque can implement circular systems.

Examples:

- Round-robin scheduling
- Team rotation
- Turn-based games
- Resource allocation

---

## Log Buffers

A deque can store the most recent log entries.

Example:

```python
deque(maxlen=100)
```

Only the latest 100 logs are preserved.

---

## Personal Project Ideas

### Rabbit Manager

- Processing queue
- Recent actions history

### Trend Tracker

- Latest trends
- Rolling history

### Medika

- Recent searches
- Recent medicines viewed

### Event Manager

- Rotation of recurring events
- Recent event history

---

## Conclusion

A deque is particularly useful when:

- Working with queues
- Working with stacks
- Keeping recent history
- Managing circular systems
- Limiting stored data with `maxlen`