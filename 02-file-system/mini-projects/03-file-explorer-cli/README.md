# File Explorer CLI

A simple command-line tool that explores a temporary workspace and displays information about files and directories using Python's `pathlib` module.

The workspace is automatically created when the program starts and automatically removed when the program exits.

## Learning Objectives

This mini-project was built to practice:

- `tempfile.TemporaryDirectory()`
- `pathlib.Path`
- File exploration
- Directory exploration
- File metadata
- File searching
- Input validation
- CLI menus

---

## Features

- Create a temporary workspace automatically.
- Create sample files and directories.
- List all files.
- List all directories.
- Display file information.
- Search files by extension.
- Automatically clean the workspace on exit.

---

## Project Structure

```text
03-file-explorer-cli/
├── README.md
└── src/
    ├── main.py
    ├── explorer.py
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
workspace/
├── documents/
│   ├── notes.txt
│   └── report.pdf
├── images/
│   ├── logo.png
│   └── photo.jpg
└── scripts/
    └── main.py
```

---

## Example Usage

```text
Workspace created:
/tmp/workspace_6a4oqnae

File Explorer CLI

1. List files
2. List directories
3. Show file information
4. Search by extension
5. Exit

Choice : 1

Workspace content (5 files):

1. main.py
2. photo.jpg
3. logo.png
4. report.pdf
5. notes.txt

Choice : 1

Name      : main.py
Extension : .py
Size      : 167 bytes
Path      : scripts/main.py

Choice : 4

Allowed extension : {'.txt', '.pdf', '.png', '.jpg', '.py'}

Enter extension : py

File(s) found.

scripts/main.py

Choice : 5

See you soon !
```

---

## Supported Extensions

```text
.txt
.pdf
.png
.jpg
.py
```

---

## Status

✅ Completed