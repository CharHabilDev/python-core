# Task Queue Manager CLI

A command-line application that manages tasks using a FIFO (First In, First Out) queue and Python collections.

## Features

- Add a task
- View pending tasks
- Process the next task (FIFO)
- View completed tasks
- Group tasks by priority
- Display task statistics
- Keep a history of recent actions

## Concepts Practiced

### deque

Used to:

- Process tasks in FIFO order
- Store recent actions
- Limit history size with `maxlen`

### namedtuple

Used to:

- Represent task records
- Access task fields by name

### defaultdict

Used to:

- Group tasks by priority

### Counter

Used to:

- Count tasks by status
- Count tasks by priority

### JSON

Used to:

- Persist tasks
- Persist recent actions

## Project Structure

```text
02-task-queue-manager-cli/
│
├── README.md
│
├── data/
│   ├── tasks.json
│   └── history.json
│
└── src/
    ├── main.py
    ├── tasks.py
    ├── storage.py
    └── utils.py
```

## Menu

```text
=== Task Manager ===

1. Add task
2. View pending tasks
3. Process next task
4. View completed tasks
5. Group tasks by priority
6. Show statistics
7. View recent actions
0. Exit
```

## Example Task

```text
ID       : T001
Title    : Finish Python Foundations
Priority : High
Status   : Pending
```

## Example Pending Tasks

```text
=== PENDING TASKS ===

ID     | PRIORITY   | TITLE
-----------------------------------------------------------
T005   | HIGH       | Build Flask Project
T006   | MEDIUM     | Read Python Documentation
T007   | LOW        | Organize Notes
```

## Example Processed Task

```text
========================================
TASK COMPLETED : T005
========================================
Title    : Build Flask Project
Priority : High
Status   : Completed
========================================
```

## Example Grouping

```text
HIGH (3)
-------------------------
Build Flask Project
Create Database Schema
Write Unit Tests

MEDIUM (2)
-------------------------
Read Python Documentation
Refactor Contact Manager

LOW (1)
-------------------------
Organize Notes
```

## Example Statistics

```text
=== TASK STATISTICS ===

By Status

Pending   : 6
Completed : 4

By Priority

High      : 4
Medium    : 3
Low       : 3
```

## Example Recent Actions

```text
[+] T006 - Read Python Documentation
[+] T007 - Organize Notes
[✓] T001 - Finish Python Foundations
[✓] T004 - Update GitHub README
[✓] T009 - Refactor Contact Manager
```

## Requirements

- Python 3.12+

## Run

```bash
python -m src.main
```

## Learning Goals

This project was created to practice:

- FIFO queues
- Data grouping
- Data counting
- JSON persistence
- Modular programming
- CLI application design
- Python collections (`deque`, `namedtuple`, `defaultdict`, `Counter`)