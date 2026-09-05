# Converting Time Zones

## Goal

Learn how to convert an aware datetime from one timezone to another.

## Key Concepts

### Convert a timezone

```python
datetime.astimezone(...)
```

### Example

```python
brussels_time.astimezone(ZoneInfo("Asia/Tokyo"))
```

### Important

- The moment does not change.
- The displayed local time changes.
- The result is still an aware datetime.

## Remember

- `ZoneInfo()` adds timezone information.
- `astimezone()` converts between timezones.
- Different local times can represent the same moment.