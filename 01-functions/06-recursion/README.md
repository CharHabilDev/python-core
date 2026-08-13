# Recursion

## Introduction

Recursion is a programming technique where a function calls itself.

Instead of using a loop, a recursive function solves a problem by breaking it into smaller versions of the same problem.

Every recursive function must have:

- a base case;
- a recursive case.

Without a base case, recursion would continue indefinitely.

---

## Base Case

The base case stops the recursion.

```python
def compte_a_rebours(n):

    if n == 0:
        print("Décollage !")
        return

    print(n)
    compte_a_rebours(n - 1)
```

The condition:

```python
if n == 0:
```

is the base case.

---

## Recursive Case

The recursive case is the part where the function calls itself.

```python
compte_a_rebours(n - 1)
```

Each call moves closer to the base case.

---

## Countdown Example

```python
def compte_a_rebours(n):

    if n == 0:
        print("Décollage !")
        return

    print(n)
    compte_a_rebours(n - 1)
```

Usage:

```python
compte_a_rebours(5)
```

Output:

```text
5
4
3
2
1
Décollage !
```

---

## Factorial Example

Mathematical definition:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive implementation:

```python
def factorielle(n):

    if n == 1:
        return 1

    return n * factorielle(n - 1)
```

Usage:

```python
print(factorielle(5))
```

Output:

```text
120
```

---

## Recursive Sum Example

```python
def somme(n):

    if n == 0:
        return 0

    return n + somme(n - 1)
```

Usage:

```python
print(somme(5))
```

Calculation:

```text
5 + 4 + 3 + 2 + 1
```

Output:

```text
15
```

---

## How Recursion Works

Example:

```python
factorielle(4)
```

Python evaluates:

```text
4 * factorielle(3)
4 * (3 * factorielle(2))
4 * (3 * (2 * factorielle(1)))
4 * (3 * (2 * 1))
```

Then:

```text
24
```

The recursive calls are stacked until the base case is reached, then Python resolves them in reverse order.

---

## Recursion vs Loops

Recursive version:

```python
def compte_a_rebours(n):

    if n == 0:
        return

    print(n)
    compte_a_rebours(n - 1)
```

Loop version:

```python
for n in range(5, 0, -1):
    print(n)
```

Both approaches solve the same problem.

For simple repetition, loops are often easier to read.

---

## Advantages

- Elegant for certain problems.
- Matches many mathematical definitions.
- Useful for hierarchical structures.
- Helps understand function calls and execution flow.

---

## Disadvantages

- Can be harder to understand.
- Often slower than loops.
- Uses more memory.
- May trigger recursion limits.

Example:

```python
def infinite():
    infinite()
```

Output:

```text
RecursionError: maximum recursion depth exceeded
```

---

## Common Use Cases

Recursion is commonly used for:

- factorial calculations;
- Fibonacci sequences;
- tree structures;
- file and directory traversal;
- searching hierarchical data;
- nested structures.

---

## Best Practices

✅ Always define a base case.

✅ Ensure every recursive call moves closer to the base case.

✅ Prefer loops when recursion adds unnecessary complexity.

❌ Never write recursion without a stopping condition.

---

## Key Takeaways

- Recursion is when a function calls itself.
- Every recursive function requires a base case.
- The recursive case moves toward the base case.
- Recursive calls are stacked and resolved in reverse order.
- Recursion is useful for hierarchical and nested problems.
- Poor recursion design can lead to `RecursionError`.