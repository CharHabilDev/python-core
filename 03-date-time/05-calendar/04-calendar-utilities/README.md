# Calendar Utilities

## Goal

Learn how to retrieve information about months and leap years.

## Main Concepts

### Days in a Month

```python
calendar.monthrange(year, month)
```

Returns:

```python
(first_weekday, number_of_days)
```

### Leap Years

```python
calendar.isleap(year)
```

Returns:

```python
True
False
```

## Remember

- `monthrange()` returns weekday and number of days.
- `isleap()` checks leap years.
- February can have 28 or 29 days.