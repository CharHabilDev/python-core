# File System Cheat Sheet

Quick reference for:

- os
- platform
- pathlib
- shutil
- tempfile

---

# os

## Current Directory

```python
os.getcwd()
```

Get current working directory.

```python
os.chdir(path)
```

Change current directory.

---

## Directories

```python
os.mkdir(path)
```

Create directory.

```python
os.rmdir(path)
```

Remove empty directory.

```python
os.listdir(path)
```

List directory contents.

---

## Environment Variables

```python
os.getenv("HOME")
```

Get environment variable.

```python
os.environ
```

Access environment variables.

---

## Useful

```python
os.name
```

Operating system family.

---

# platform

## System Information

```python
platform.system()
```

Operating system name.

```python
platform.release()
```

OS version.

```python
platform.platform()
```

Detailed platform information.

```python
platform.machine()
```

Machine architecture.

```python
platform.architecture()
```

Python architecture.

---

## Python Information

```python
platform.python_version()
```

Python version.

```python
platform.python_implementation()
```

Python implementation.

---

# pathlib

## Create Paths

```python
Path("folder")
```

```python
Path("folder") / "file.txt"
```

Join paths.

---

## Existence

```python
path.exists()
```

Check existence.

```python
path.is_file()
```

Check file.

```python
path.is_dir()
```

Check directory.

---

## Create

```python
path.mkdir()
```

Create directory.

```python
path.mkdir(
    parents=True,
    exist_ok=True
)
```

Create nested directories.

```python
path.touch()
```

Create file.

---

## Iteration

```python
path.iterdir()
```

List contents.

```python
path.rglob("*")
```

Recursive search.

---

## Read / Write

```python
path.write_text()
```

Write text.

```python
path.read_text()
```

Read text.

---

## Delete

```python
path.unlink()
```

Delete file.

```python
path.rmdir()
```

Delete empty directory.

---

# shutil

## Copy Files

```python
shutil.copy()
```

Copy file.

```python
shutil.copy2()
```

Copy file + metadata.

---

## Copy Directories

```python
shutil.copytree()
```

Copy directory tree.

```python
shutil.copytree(
    source,
    destination,
    dirs_exist_ok=True
)
```

Overwrite existing destination.

---

## Move / Rename

```python
shutil.move()
```

Move file or directory.

Rename file or directory.

---

## Remove

```python
shutil.rmtree()
```

Delete directory tree.

---

## Archives

```python
shutil.make_archive()
```

Create archive.

```python
shutil.unpack_archive()
```

Extract archive.

---

# tempfile

## Temporary File

```python
tempfile.TemporaryFile()
```

Anonymous temporary file.

```python
tempfile.NamedTemporaryFile()
```

Temporary file with visible name.

---

## Temporary Directory

```python
tempfile.TemporaryDirectory()
```

Temporary directory.

---

## Context Manager

```python
with tempfile.TemporaryFile() as temp:
```

Automatic cleanup.

```python
with tempfile.TemporaryDirectory() as temp_dir:
```

Automatic cleanup.

---

# Quick Guide

## Need...

### System information

```python
platform
```

### Environment variables

```python
os
```

### Path manipulation

```python
pathlib
```

### Copy / Move / Archive

```python
shutil
```

### Temporary files

```python
tempfile
```

---

# Common Workflow

```text
Path()
↓
Build path

exists()
↓
Check existence

copytree()
↓
Backup

make_archive()
↓
ZIP

TemporaryDirectory()
↓
Temporary workspace
```