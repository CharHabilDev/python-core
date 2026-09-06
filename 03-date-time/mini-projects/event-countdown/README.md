# Event Countdown

A simple CLI application that calculates the remaining time until a future event.

## Features

- Calculate remaining days until an event
- Display a detailed countdown
- Validate user input
- Reject past dates
- Handle events occurring today

---

## Concepts Practiced

- `datetime`
- `timedelta`
- `strptime()`
- `strftime()`
- Date comparisons
- Input validation
- Functions

---

## Project Structure

```text
event-countdown/
│
├── src/
│   ├── main.py
│   ├── countdown.py
│   └── utils.py
│
└── README.md
```

---

## Run

```bash
python -m src.main
```

---

## Menu

```text
=== Event Countdown ===

1. Days Remaining
2. Detailed Countdown
0. Exit
```

---

## Example

```text
Choice: 1

Enter event date (dd/mm/yyyy): 25/12/2026

Event in 110 days.

Choice: 2

Enter event date (dd/mm/yyyy): 25/12/2026

Event date : 25/12/2026
Remaining : 110 days, 12 hours, 35 minutes, 10 seconds.
```

---

## Status

✅ Completed