# *args and **kwargs

## Introduction

Sometimes a function needs to accept a variable number of arguments.

Instead of defining many parameters manually, Python provides:

- `*args` for positional arguments;
- `**kwargs` for keyword arguments.

These features make functions more flexible and reusable.

---

## *args

`*args` collects extra positional arguments into a tuple.

```python
def addition(*args):
    print(args)
```

Example:

```python
addition(1, 2, 3)
```

Output:

```text
(1, 2, 3)
```

Python automatically creates a tuple containing all positional arguments.

---

## Using *args

A common use case is processing an unknown number of values.

```python
def addition(*args):
    total = 0

    for number in args:
        total += number

    return total
```

Examples:

```python
addition(1, 2)
addition(1, 2, 3)
addition(1, 2, 3, 4, 5)
```

---

## Naming *args

The name `args` is only a convention.

The following examples are equivalent:

```python
def addition(*args):
    pass
```

```python
def addition(*numbers):
    pass
```

What matters is the `*` symbol.

---

## **kwargs

`**kwargs` collects keyword arguments into a dictionary.

```python
def afficher(**kwargs):
    print(kwargs)
```

Example:

```python
afficher(
    nom="Ali",
    age=20
)
```

Output:

```python
{
    "nom": "Ali",
    "age": 20
}
```

Python automatically creates a dictionary.

---

## Using **kwargs

```python
def afficher_profil(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

Example:

```python
afficher_profil(
    nom="Ali",
    age=20,
    ville="Cotonou"
)
```

Output:

```text
nom: Ali
age: 20
ville: Cotonou
```

---

## Naming **kwargs

Just like `args`, the name `kwargs` is only a convention.

```python
def afficher(**kwargs):
    pass
```

```python
def afficher(**utilisateur):
    pass
```

Both are valid.

What matters is the `**` symbol.

---

## Combining *args and **kwargs

A function can use both.

```python
def afficher(*args, **kwargs):

    print(args)
    print(kwargs)
```

Example:

```python
afficher(
    1,
    2,
    3,
    nom="Ali",
    age=20
)
```

Output:

```python
(1, 2, 3)

{
    "nom": "Ali",
    "age": 20
}
```

---

## Common Use Cases

Use `*args` when:

- the number of positional arguments is unknown;
- you want a flexible function interface.

Use `**kwargs` when:

- optional information may vary;
- you need named configuration values;
- you want to accept many keyword arguments.

---

## Key Takeaways

- `*args` collects positional arguments.
- `*args` creates a tuple.
- `**kwargs` collects keyword arguments.
- `**kwargs` creates a dictionary.
- The names `args` and `kwargs` are conventions.
- The symbols `*` and `**` are what give them their behavior.
- Both can be used in the same function.