# Decorators

## Introduction

A decorator is a function that modifies or extends the behavior of another function without changing its source code.

Decorators are widely used in Python frameworks and libraries such as Flask, FastAPI, pytest, and dataclasses.

---

## Functions Are Objects

In Python, functions are first-class objects.

They can be:

- assigned to variables;
- passed as arguments;
- returned from other functions.

Example:

```python
def saluer():
    print("Bonjour")

fonction = saluer

fonction()
```

Output:

```text
Bonjour
```

---

## Functions as Arguments

A function can receive another function as a parameter.

```python
def saluer():
    print("Bonjour")

def executer(fonction):
    fonction()

executer(saluer)
```

Output:

```text
Bonjour
```

Notice:

```python
executer(saluer)
```

and not:

```python
executer(saluer())
```

because we pass the function itself.

---

## Functions Returning Functions

A function can create and return another function.

```python
def creer_message():

    def saluer():
        print("Bonjour")

    return saluer
```

Usage:

```python
fonction = creer_message()

fonction()
```

Output:

```text
Bonjour
```

---

## What Is a Decorator?

A decorator receives a function and returns a modified version of that function.

Example:

```python
def decorateur(func):

    def wrapper():
        print("--- Début ---")

        func()

        print("--- Fin ---")

    return wrapper
```

---

## Applying a Decorator

Without decorator syntax:

```python
def saluer():
    print("Bonjour")

saluer = decorateur(saluer)

saluer()
```

Output:

```text
--- Début ---
Bonjour
--- Fin ---
```

---

## The `@` Syntax

Python provides a cleaner syntax:

```python
@decorateur
def saluer():
    print("Bonjour")
```

Equivalent to:

```python
def saluer():
    print("Bonjour")

saluer = decorateur(saluer)
```

---

## Why Use a Wrapper?

The wrapper function adds extra behavior before or after the original function executes.

```python
def wrapper():

    print("Avant")

    func()

    print("Après")
```

The original function remains unchanged.

---

## Decorators with Parameters

To support functions that receive arguments:

```python
def decorateur(func):

    def wrapper(*args, **kwargs):

        print("Exécution")

        return func(*args, **kwargs)

    return wrapper
```

Example:

```python
@decorateur
def addition(a, b):
    return a + b

print(addition(3, 4))
```

Output:

```text
Exécution
7
```

---

## Real-World Examples

### Flask

```python
@app.route("/")
def accueil():
    pass
```

---

### FastAPI

```python
@app.get("/")
def accueil():
    pass
```

---

### Pytest

```python
@pytest.fixture
```

---

### Dataclasses

```python
@dataclass
class User:
    ...
```

---

## Advantages

- Reuse code.
- Keep functions clean.
- Add behavior without modifying existing code.
- Improve maintainability.

---

## Common Use Cases

Decorators are commonly used for:

- logging;
- authentication;
- permissions;
- caching;
- validation;
- routing in web frameworks;
- testing utilities.

---

## Best Practices

✅ Use decorators for reusable behavior.

✅ Keep decorators simple.

✅ Use `*args` and `**kwargs` when decorating functions with parameters.

❌ Avoid overly complex decorators.

❌ Do not use decorators when a simple function call is sufficient.

---

## Key Takeaways

- Functions are first-class objects in Python.
- Functions can receive and return other functions.
- A decorator modifies a function without changing its code.
- `wrapper()` contains the added behavior.
- `@decorateur` is shorthand for:

```python
fonction = decorateur(fonction)
```

- Decorators are heavily used in Flask, FastAPI, pytest, and many Python libraries.