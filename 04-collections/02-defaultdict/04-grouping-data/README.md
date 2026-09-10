# Grouping Data

## Summary

### Purpose

Group multiple values under the same key.

### Common Pattern

```txt
key
↓
defaultdict(list)
↓
[]
↓
append(value)
```

### Typical Uses

- Students by class
- Expenses by category
- Events by month
- Rabbits by breed

### Benefits

- Automatic initialization
- Cleaner code
- No KeyError