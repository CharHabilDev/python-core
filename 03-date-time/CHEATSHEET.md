# Date & Time Cheat Sheet

## Import

```python
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar
```

---

## Current Date and Time

```python
datetime.now()
datetime.today()
date.today()
```

---

## Create a Datetime

```python
datetime(2026, 10, 5, 14, 30)
```

---

## String ↔ Datetime

### String to Datetime

```python
datetime.strptime(
    "05/10/2026",
    "%d/%m/%Y"
)
```

### Datetime to String

```python
dt.strftime("%d/%m/%Y")
```

---

## Common Format Codes

| Code | Meaning |
|------|---------|
| `%d` | Day |
| `%m` | Month |
| `%Y` | Year |
| `%H` | Hour (24h) |
| `%M` | Minute |
| `%S` | Second |

Example:

```python
"%d/%m/%Y"
```

↓

```text
05/10/2026
```

---

## Date Comparison

```python
date1 > date2
date1 < date2
date1 == date2
```

---

## Timedelta

### Difference Between Dates

```python
future_date - datetime.now()
```

### Create a Duration

```python
timedelta(days=7)
timedelta(hours=2)
```

### Access Values

```python
delta.days
delta.seconds
delta.total_seconds()
```

---

## Time Zones

### UTC

```python
ZoneInfo("UTC")
```

### Brussels

```python
ZoneInfo("Europe/Brussels")
```

### Porto-Novo

```python
ZoneInfo("Africa/Porto-Novo")
```

### Aware Datetime

```python
datetime.now(
    ZoneInfo("UTC")
)
```

---

## Convert Time Zones

```python
dt.astimezone(
    ZoneInfo("Asia/Tokyo")
)
```

---

## Calendar

### Display a Month

```python
calendar.month(
    2026,
    10
)
```

### Day Names

```python
calendar.day_name[0]
```

↓

```text
Monday
```

### Days in a Month

```python
calendar.monthrange(
    2026,
    10
)
```

Returns:

```text
(first_weekday, days)
```

Example:

```python
calendar.monthrange(
    2026,
    10
)
```

↓

```python
(3, 31)
```

### Leap Year

```python
calendar.isleap(2024)
```

↓

```python
True
```

---

## Concepts

### Naive Datetime

```python
datetime.now()
```

No timezone information.

### Aware Datetime

```python
datetime.now(
    ZoneInfo("UTC")
)
```

Contains timezone information.

### UTC

Reference time used worldwide.