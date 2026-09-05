# ZoneInfo

## Goal

Learn how to create timezone-aware datetimes.

## Key Concepts

### Import

```python
from zoneinfo import ZoneInfo
```

### Create an aware datetime

```python
datetime.now(ZoneInfo("Europe/Brussels"))
```

### Common Time Zones

- UTC
- Europe/Brussels
- Africa/Porto-Novo
- America/New_York
- Asia/Tokyo

## Remember

- `datetime.now()` → naive datetime
- `datetime.now(ZoneInfo(...))` → aware datetime
- `ZoneInfo()` adds timezone information