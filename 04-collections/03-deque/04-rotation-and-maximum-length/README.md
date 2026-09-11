# Rotation and Maximum Length

## Summary

### Rotation

`rotate()` moves elements from one end of the deque to the other.

```python
rotate(1)
rotate(-1)
```

### Rotation Directions

```text
rotate(1)

[1] [2] [3] [4]

↓

[4] [1] [2] [3]
```

```text
rotate(-1)

[1] [2] [3] [4]

↓

[2] [3] [4] [1]
```

### Maximum Size

A deque can have a fixed maximum size using `maxlen`.

```python
deque(maxlen=5)
```

### Automatic Removal

When the maximum size is reached, the oldest element is automatically removed.

```text
maxlen = 3

[A] [B] [C]

append(D)

↓

[B] [C] [D]
```

### Typical Uses

#### rotate()

- Round-robin scheduling
- Turn-based games
- Team rotation
- Circular processing

#### maxlen

- Recent searches
- Browser history
- Notifications
- Log buffers
- Last N events

### Key Features

```python
rotate()

maxlen
```