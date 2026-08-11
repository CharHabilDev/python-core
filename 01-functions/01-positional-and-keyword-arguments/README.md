# Positional and Keyword Arguments

## Introduction

When calling a function in Python, values can be passed to parameters in different ways.

The two most common approaches are:

- positional arguments;
- keyword arguments.

Understanding the difference between them is essential for writing clear and flexible functions.

---

## Parameters and Arguments

A **parameter** is a variable defined in a function.

```python
def greet(name):
    print(f"Hello {name}")
```

Here, `name` is a parameter.

An **argument** is the value passed to a function when it is called.

```python
greet("Ali")
```

Here, `"Ali"` is an argument.

---

## Positional Arguments

Positional arguments are assigned according to their order.

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Fatima", 25)
```

Python assigns:

```text
name = "Fatima"
age = 25
```

The order matters.

```python
introduce(25, "Fatima")
```

This produces an incorrect result because the values are assigned to the wrong parameters.

---

## Keyword Arguments

Keyword arguments explicitly specify the parameter names.

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(name="Fatima", age=25)
```

Python assigns values using the parameter names instead of their position.

The order no longer matters.

```python
introduce(age=25, name="Fatima")
```

This works correctly.

---

## Mixing Positional and Keyword Arguments

Python allows both styles in the same function call.

```python
introduce("Fatima", age=25)
```

However, positional arguments must come before keyword arguments.

✅ Correct:

```python
introduce("Fatima", age=25)
```

❌ Incorrect:

```python
introduce(name="Fatima", 25)
```

---

## When to Use Each

Use positional arguments when:

- the meaning is obvious;
- the function has only a few parameters.

Use keyword arguments when:

- readability is important;
- a function has many parameters;
- you want to avoid mistakes caused by parameter order.

---

## Key Takeaways

- A parameter is defined in a function.
- An argument is a value passed to a function.
- Positional arguments depend on order.
- Keyword arguments depend on parameter names.
- Keyword arguments improve readability.
- Positional arguments must come before keyword arguments when both are used.