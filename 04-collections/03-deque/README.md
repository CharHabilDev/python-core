# Deque

`deque` (double-ended queue) is a specialized container that allows fast insertion and removal of elements from both ends.

Unlike a standard list, a deque is optimized for operations at the beginning and the end of a sequence.

## Learning Objectives

After completing this chapter, I should be able to:

- Understand what a deque is.
- Create and manipulate a deque.
- Add and remove elements efficiently.
- Use deque-specific methods.
- Identify real-world use cases for deque.

---

## Topics

| # | Topic | Status |
|---|-------|:------:|
| 1 | Introduction | ✅ |
| 2 | Creating a Deque | ⬜ |
| 3 | Adding and Removing Elements | ⬜ |
| 4 | Rotation and Maximum Length | ⬜ |
| 5 | Real-World Use Cases | ⬜ |

---

## Common Use Cases

- Task queues
- Browser history
- Undo/Redo systems
- Sliding window algorithms
- Message processing
- Log buffering

---

## Key Idea

```text
Left End  ←  deque  →  Right End

appendleft()
popleft()

append()
pop()
```

A deque provides efficient operations on both sides of the container.

---

## Status

⬜ In Progress