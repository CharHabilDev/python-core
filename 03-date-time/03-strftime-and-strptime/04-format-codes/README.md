# Format Codes

Format codes are used by `strftime()` and `strptime()` to represent specific parts of dates and times.

They allow Python applications to format and parse dates consistently.

## Essential Syntax

```python
date.strftime("%d/%m/%Y")
datetime.strptime("25/12/2026", "%d/%m/%Y")
```

## Key Concepts

- `%Y` year (4 digits)
- `%y` year (2 digits)
- `%m` month
- `%d` day
- `%H` hour
- `%M` minute
- `%S` second

---

## Status

✅ Completed