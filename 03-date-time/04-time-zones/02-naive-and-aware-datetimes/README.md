# Naive and Aware Datetimes

Python provides two types of datetime objects:

- naive datetimes
- aware datetimes

## Key Difference

| Type   | Time Zone |
|--------|:---------:|
| Naive  | ❌        |
| Aware  | ✅        |

## Example

```python
datetime(2026, 1, 1, 15, 0)  # naive
```

```text
2026-01-01 15:00 UTC+1  # aware
```

## Summary

- Naive → no time zone information
- Aware → time zone included
- Aware datetimes are preferred for international applications

---

## Status

✅ Completed