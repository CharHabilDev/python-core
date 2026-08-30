# Backup Utility

A simple command-line tool that creates backups of files and directories using Python's `pathlib` and `shutil` modules.

A temporary workspace is automatically created when the program starts and removed when the program exits.

## Learning Objectives

This mini-project was built to practice:

- `pathlib.Path`
- `shutil.copy2()`
- `shutil.copytree()`
- Directory creation
- File and directory traversal
- CLI menus
- File backups
- Directory backups
- Workspace cleanup

---

## Features

- Create a temporary test workspace.
- Backup individual files.
- Backup complete directories.
- List available files and directories.
- List existing backups.
- Automatically clean the workspace on exit.

---

## Project Structure

```text
02-backup-utility/
├── README.md
└── src/
    ├── main.py
    ├── backup.py
    └── utils.py
```

---

## Run

```bash
python -m src.main
```

---

## Test Workspace

The application automatically creates the following structure:

```text
sandbox/
├── documents/
│   ├── notes.txt
│   └── todo.md
└── project/
    ├── main.py
    └── config.json
```

---

## Example Usage

```text
Workspace created: /tmp/sandbox_kjxgd7w8

Backup Utility

1. Backup file
2. Backup directory
3. List backups
4. Exit

Choice : 1

Available files:

1. documents/notes.txt
2. documents/todo.md
3. project/main.py
4. project/config.json

Backup choice : 1

File backup successful.

Choice : 3

Backups content (1 items):

notes.txt

Choice : 4

Cleaning sandbox...
See you soon!
```

---

## Technologies

- Python 3
- tempfile
- pathlib
- shutil

---

## Status

✅ Completed