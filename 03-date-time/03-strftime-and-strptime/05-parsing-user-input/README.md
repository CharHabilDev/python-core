# Parsing User Input

User input is usually received as strings.

To work with dates, applications often convert user-provided text into datetime objects using `strptime()`.

## Essential Syntax

```python
user_input = input("Date: ")
date = datetime.strptime(user_input, "%d/%m/%Y")
```

## Key Concepts

- user input
- string parsing
- datetime conversion
- validation
- date comparison

---

## Status

✅ Completed