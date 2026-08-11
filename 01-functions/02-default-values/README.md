# Default Values

## Introduction

Default values allow a function parameter to become optional.

When no argument is provided, Python automatically uses the default value defined in the function.

This makes functions more flexible and easier to use.

---

## Defining a Default Value

A default value is assigned using the `=` operator in the function definition.

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

If no argument is provided:

```python
greet()
```

Output:

```text
Hello Guest
```

If an argument is provided, it replaces the default value:

```python
greet("Ali")
```

Output:

```text
Hello Ali
```

---

## Multiple Default Values

A function can have several optional parameters.

```python
def create_event(title, location="Undefined", capacity=50):
    print(f"{title} - {location} - {capacity}")
```

Examples:

```python
create_event("Hackathon")
create_event("Hackathon", "Cotonou")
create_event("Hackathon", "Cotonou", 200)
```

---

## Default Values with Keyword Arguments

Default values work perfectly with keyword arguments.

```python
def create_user(username, role="user"):
    print(f"{username} - {role}")
```

```python
create_user(username="charles")
create_user(username="charles", role="admin")
```

---

## Required and Optional Parameters

Parameters without default values are required.

```python
def create_user(username):
    pass
```

The function cannot be called without providing `username`.

Parameters with default values are optional.

```python
def create_user(username, role="user"):
    pass
```

The function can now be called with only `username`.

---

## Parameter Order

Required parameters must come before optional parameters.

✅ Correct

```python
def create_user(username, role="user"):
    pass
```

❌ Incorrect

```python
def create_user(role="user", username):
    pass
```

Python raises a syntax error because it cannot determine how arguments should be assigned.

---

## Common Pattern: None

A common Python practice is to use `None` as a default value.

```python
def create_expense(category, amount, expense_date=None):
    pass
```

Inside the function:

```python
if expense_date is None:
    expense_date = get_current_date()
```

This pattern is widely used in real-world Python applications.

---

## When to Use Default Values

Use default values when:

- a parameter has a common value;
- a parameter should be optional;
- you want to simplify function calls;
- you want to provide sensible defaults.

---

## Key Takeaways

- Default values make parameters optional.
- A provided argument overrides the default value.
- Required parameters must come before optional parameters.
- `None` is commonly used as a default value.
- Default values improve flexibility and readability.