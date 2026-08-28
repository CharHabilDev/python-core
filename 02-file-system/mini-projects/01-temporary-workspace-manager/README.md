# Temporary Workspace Manager

A simple command-line tool that creates and manages a temporary workspace using Python's `tempfile` module.

The workspace is automatically created when the program starts and automatically removed when the program exits.

## Learning Objectives

This mini-project was built to practice:

- `tempfile.TemporaryDirectory()`
- `pathlib.Path`
- File creation
- Directory navigation
- Input validation
- CLI menus
- Automatic cleanup with temporary resources

---

## Features

- Create a temporary workspace automatically.
- Create files inside the workspace.
- Validate file extensions.
- List workspace files.
- Automatically delete the workspace on exit.

---

## Project Structure

```text
01-temporary-workspace-manager/
├── README.md
└── src/
    ├── main.py
    ├── workspace.py
    └── utils.py
```

---

## Run

```bash
python -m src.main
```

---

## Supported File Types

Files are restricted to a predefined set of extensions for validation purposes.

---

## Example Usage

```txt
Workspace created:
/tmp/workspace_abcd1234

Temporary Workspace Manager

1. Create file
2. List files
3. Exit

Choice : 1
Accepted file type : {'.txt', '.docx', '.md', '.doc', '.py'}
File name : notes.txt

File 'notes.txt' created.

Choice : 2

Files:

Number of files: 1
notes.txt

Choice : 3
See you soon !
```

---

## Technologies

- Python 3
- tempfile
- pathlib

---

## Status

✅ Completed