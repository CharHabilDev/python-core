# Contact Manager CLI

A command-line application for managing contacts using Python collections and JSON persistence.

## Features

- Add a contact
- View all contacts
- Search a contact by ID
- Group contacts by city
- Show contact statistics
- View recent searches
- Store contacts in JSON files

## Requirements

- Python 3.12+

## Run

```bash
python -m src.main
```

## Menu

```text
1. Add a contact
2. View all contacts
3. Search a contact
4. Group contacts by city
5. Show contact statistics
6. View recent searches
0. Exit
```

## Contact Structure

Each contact contains:

```text
ID
Name
Phone
Email
City
```

Example:

```text
N001
Alice
+2290144752517
alice@email.com
Cotonou
```

## Example Contact List

```text
-------------------------------------------------------------------------------------
|  ID  |      Name       |      Phone      |          Email           |    City     |
-------------------------------------------------------------------------------------
| N001 | Alice           | +2290144752517  | alice@email.com          | Cotonou     |
| N002 | Thomas          | +32471234567    | thomas@email.com         | Brussels    |
-------------------------------------------------------------------------------------
```

## Example Statistics

```text
=== CONTACT STATISTICS ===

Total contacts      : 5
Unique cities       : 3

Contacts by city

Brussels            : 2
Cotonou             : 2
Paris               : 1

Most represented city : Brussels (2 contacts)
```

## Example Grouping

```text
Group Contacts By City

Brussels
├─ Thomas
├─ Yasmine

Cotonou
├─ Alice
├─ David

Paris
├─ Sarah
```

## Example Recent Searches

```text
=== Recent Searches ===

1. Alice
2. Thomas
3. David
4. Sarah
5. Yasmine
```

## Data Files

```text
data/
├── contacts.json
└── history.json
```

### contacts.json

Stores contact records.

### history.json

Stores the last 5 searches using a deque with `maxlen=5`.

## Concepts Practiced

### namedtuple

Used to:

- Represent contacts
- Access data by field name
- Improve readability

### defaultdict

Used to:

- Group contacts by city

### Counter

Used to:

- Count contacts by city
- Generate statistics

### deque

Used to:

- Store recent searches
- Limit history size with `maxlen`

### JSON

Used to:

- Persist contacts
- Persist search history

## Project Structure

```text
contact-manager-cli/
│
├── README.md
│
├── data/
│   ├── contacts.json
│   └── history.json
│
├── src/
│   ├── contacts.py
│   ├── storage.py
│   ├── utils.py
│   └── main.py
│
└── .gitignore
```

## Learning Goals

This project was created to practice:

- Modular programming
- Data validation
- File handling
- JSON persistence
- Python collections
  - namedtuple
  - defaultdict
  - Counter
  - deque
- CLI application design