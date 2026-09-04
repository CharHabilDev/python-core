# Introduction

Time zones allow applications to represent the same instant differently depending on a user's location.

A date and time alone are not always enough. Without a time zone, it may be impossible to know exactly when an event occurs for users in different countries.

## Key Concepts

### UTC

UTC (Coordinated Universal Time) is the global time reference.

Examples:

- UTC+1
- UTC+2
- UTC-5
- UTC+9

### Time Zone

A time zone is a region that uses the same local time.

Examples:

- Brussels → UTC+1
- Cotonou → UTC+1
- Tokyo → UTC+9
- New York → UTC-5

### Same Instant, Different Times

```text
UTC : 12:00

Cotonou : 13:00

Tokyo : 21:00

New York : 07:00
```

These times can represent the same moment.

## Why Time Zones Matter

Applications that commonly use time zones:

- calendars
- messaging systems
- flight reservations
- video meetings
- social networks
- cloud services

Without proper time zone handling:

- meetings may occur at the wrong time
- notifications may be delayed
- reservations may be incorrect
- message timestamps may become confusing

---

## Status

✅ Completed