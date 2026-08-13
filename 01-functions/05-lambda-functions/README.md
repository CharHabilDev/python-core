# Lambda Functions

## Introduction

A lambda function is a small anonymous function.

Lambda functions are useful when a function is needed only once and the logic is simple.

They are commonly used with functions such as:

- `sorted()`
- `max()`
- `min()`
- `map()`
- `filter()`

---

## Syntax

A lambda function is defined using the `lambda` keyword.

```python
lambda parameters: expression
```

Example:

```python
lambda x: x * 2
```

This function receives a value and returns its double.

---

## Lambda vs Regular Function

Regular function:

```python
def double(x):
    return x * 2
```

Equivalent lambda:

```python
double = lambda x: x * 2
```

Usage:

```python
print(double(5))
```

Output:

```text
10
```

---

## Multiple Parameters

Lambda functions can accept multiple parameters.

```python
addition = lambda a, b: a + b
```

Usage:

```python
print(addition(10, 5))
```

Output:

```text
15
```

---

## Using Lambda with sorted()

Lambda functions are often used as sorting keys.

```python
names = [
    "Omar",
    "Ali",
    "Fatima",
    "Youssouf"
]
```

Sort by length:

```python
sorted_names = sorted(
    names,
    key=lambda name: len(name)
)
```

Result:

```python
[
    "Ali",
    "Omar",
    "Fatima",
    "Youssouf"
]
```

---

## Using Lambda with max()

```python
products = [
    {"name": "SSD", "price": 100},
    {"name": "Screen", "price": 250},
    {"name": "Keyboard", "price": 50}
]
```

Find the most expensive product:

```python
most_expensive = max(
    products,
    key=lambda product: product["price"]
)
```

Result:

```python
{
    "name": "Screen",
    "price": 250
}
```

---

## Using Lambda with min()

```python
cheapest = min(
    products,
    key=lambda product: product["price"]
)
```

Result:

```python
{
    "name": "Keyboard",
    "price": 50
}
```

---

## Limitations

Lambda functions can contain only one expression.

✅ Valid:

```python
lambda x: x * 2
```

✅ Valid:

```python
lambda a, b: a + b
```

❌ Invalid:

```python
lambda x:
    print(x)
    return x * 2
```

For complex logic, use a regular function.

---

## When to Use Lambda

Use lambda when:

- the operation is simple;
- the function is used only once;
- a function is needed as an argument.

Avoid lambda when:

- the logic is complex;
- multiple statements are required;
- readability suffers.

---

## Best Practices

✅ Keep lambda functions short.

✅ Use them with `sorted()`, `max()`, and `min()`.

✅ Prefer regular functions for complex operations.

❌ Do not replace every function with a lambda.

---

## Key Takeaways

- A lambda function is an anonymous function.
- Lambda functions are written in a single expression.
- They automatically return the result of that expression.
- They are commonly used with sorting and filtering operations.
- Regular functions are usually better for complex logic.