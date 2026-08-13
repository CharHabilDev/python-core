# Generators

## Introduction

A generator is a special type of function that produces values one at a time instead of returning them all at once.

Generators are useful when working with large amounts of data because they help reduce memory usage.

Generators use the `yield` keyword.

---

## The `yield` Keyword

Unlike `return`, which ends a function immediately, `yield` pauses the function and remembers its state.

Example:

```python
def nombres():
    yield 1
    yield 2
    yield 3
```

Usage:

```python
for nombre in nombres():
    print(nombre)
```

Output:

```text
1
2
3
```

---

## `yield` vs `return`

Using `return`:

```python
def nombres():
    return [1, 2, 3]
```

The entire list is created and returned immediately.

Using `yield`:

```python
def nombres():
    yield 1
    yield 2
    yield 3
```

Values are produced only when needed.

---

## Generator Objects

Calling a generator function does not execute it immediately.

```python
def nombres():
    yield 1
    yield 2
    yield 3

gen = nombres()

print(gen)
```

Output:

```text
<generator object nombres at ...>
```

A generator object is created.

---

## Using `next()`

You can manually retrieve values using `next()`.

```python
gen = nombres()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
1
2
3
```

Each call resumes execution where the generator previously stopped.

---

## StopIteration

When a generator has no more values to produce, Python raises:

```text
StopIteration
```

Example:

```python
gen = nombres()

next(gen)
next(gen)
next(gen)
next(gen)
```

Output:

```text
StopIteration
```

This indicates that the generator is exhausted.

---

## Generators with Loops

Generators are often combined with loops.

```python
def nombres():

    for i in range(1, 6):
        yield i
```

Usage:

```python
for nombre in nombres():
    print(nombre)
```

Output:

```text
1
2
3
4
5
```

---

## Example: Even Numbers

```python
def pairs(limite):

    n = 2

    while n <= limite:
        yield n
        n += 2
```

Usage:

```python
for nombre in pairs(10):
    print(nombre)
```

Output:

```text
2
4
6
8
10
```

---

## Example: Characters of a Word

```python
def lettres(mot):

    for lettre in mot:
        yield lettre
```

Usage:

```python
for lettre in lettres("python"):
    print(lettre)
```

Output:

```text
p
y
t
h
o
n
```

---

## Generator Expressions

Just as list comprehensions exist, Python provides generator expressions.

List:

```python
nombres = [x for x in range(10)]
```

Generator:

```python
nombres = (x for x in range(10))
```

Difference:

- `[]` creates a list.
- `()` creates a generator.

---

## Advantages

- Uses less memory.
- Produces values on demand.
- Useful for large datasets.
- Useful for streams of data.
- Can improve performance.

---

## Common Use Cases

Generators are commonly used for:

- reading large files;
- processing logs;
- handling API responses;
- working with large datasets;
- data pipelines;
- streaming data.

---

## Best Practices

✅ Use generators when values can be produced progressively.

✅ Use generators for large datasets.

✅ Iterate with `for` whenever possible.

❌ Do not convert generators to lists unless necessary.

❌ Do not use generators when all values must be available immediately.

---

## Key Takeaways

- Generators produce values one at a time.
- Generators use the `yield` keyword.
- `yield` pauses a function instead of stopping it.
- `next()` retrieves the next value from a generator.
- `StopIteration` means no values remain.
- Generators are memory efficient and ideal for large amounts of data.