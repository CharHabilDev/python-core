# Introduction

This chapter introduces the Python `os` module and its basic interaction with the operating system.

It provides access to information about the current environment and allows simple filesystem operations such as listing directories, creating folders, and removing empty directories.

## Learning Objectives

After completing this chapter, I should be able to:

- Import and use the `os` module.
- Identify the operating system family.
- Retrieve the current working directory.
- List directory contents.
- Create directories.
- Remove empty directories.
- Understand the difference between `os` and `pathlib`.

## Topics Covered

- `os.name`
- `os.getcwd()`
- `os.listdir()`
- `os.mkdir()`
- `os.rmdir()`

## Key Concepts

### Operating System Name

```python
import os

print(os.name)
```

Returns the operating system family:

```text
posix
```

or

```text
nt
```

### Current Working Directory

```python
os.getcwd()
```

Returns the absolute path of the current working directory.

### Listing Directory Contents

```python
os.listdir()
```

Returns a list containing the names of files and directories in the current directory.

### Creating a Directory

```python
os.mkdir("documents")
```

Creates a new directory.

### Removing an Empty Directory

```python
os.rmdir("documents")
```

Removes an empty directory.

## Comparison with pathlib

### os

```python
import os

path = os.path.join(
    "documents",
    "notes.txt"
)
```

### pathlib

```python
from pathlib import Path

path = Path("documents") / "notes.txt"
```

`pathlib` provides a more object-oriented and readable approach for path manipulation, while `os` offers broader operating system functionality.

## Common Use Cases

- Accessing system information.
- Reading environment variables.
- Managing directories.
- Interacting with the operating system.
- Supporting legacy Python codebases.

## Status

✅ Completed