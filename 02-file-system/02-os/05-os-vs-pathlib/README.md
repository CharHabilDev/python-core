# OS vs Pathlib

This chapter compares the `os` and `pathlib` modules for working with file system paths in Python.

While both modules can be used to manipulate paths and check files or directories, modern Python projects generally prefer `pathlib` because it provides a more readable and object-oriented interface.

## Learning Objectives

After completing this chapter, I should be able to:

- Understand the role of `os.path`.
- Understand the role of `pathlib`.
- Create paths using both approaches.
- Check file and directory existence.
- Compare path manipulation techniques.
- Know when to use `os` and when to use `pathlib`.
- Follow modern Python best practices for path handling.

## Topics Covered

- `os.path.join()`
- `os.path.exists()`
- `os.path.isfile()`
- `os.path.isdir()`
- `Path()`
- `Path.exists()`
- `Path.is_file()`
- `Path.is_dir()`

## Key Concepts

### Creating Paths

Using `os`:

```python
import os

path = os.path.join(
    "documents",
    "notes.txt"
)
```

Using `pathlib`:

```python
from pathlib import Path

path = Path("documents") / "notes.txt"
```

---

### Checking Existence

Using `os`:

```python
import os

os.path.exists("README.md")
```

Using `pathlib`:

```python
from pathlib import Path

Path("README.md").exists()
```

---

### Checking Files

Using `os`:

```python
os.path.isfile("notes.txt")
```

Using `pathlib`:

```python
Path("notes.txt").is_file()
```

---

### Checking Directories

Using `os`:

```python
os.path.isdir("documents")
```

Using `pathlib`:

```python
Path("documents").is_dir()
```

## Why Pathlib Was Introduced

Before Python 3.4, path manipulation relied mostly on:

```python
os.path.join(...)
```

and similar functions.

`pathlib` was introduced to:

- simplify path manipulation;
- improve readability;
- provide an object-oriented interface;
- reduce nested function calls;
- make path operations easier to understand.

## os.path vs pathlib

| Feature             | os.path | pathlib   |
| ------------------- | ------- | --------- |
| Uses strings        | ✅      | ❌        |
| Uses objects        | ❌      | ✅        |
| Readability         | Good    | Excellent |
| Modern Python style | ⚠️      | ✅        |
| Path manipulation   | ✅      | ✅        |
| File checks         | ✅      | ✅        |

## When to Use Pathlib

Prefer `pathlib` when:

- creating paths;
- navigating directories;
- checking files and folders;
- searching for files;
- writing modern Python applications.

Example:

```python
from pathlib import Path

project = Path("data") / "users.json"
```

## When to Use os

Prefer `os` when:

- working with environment variables;
- changing the current working directory;
- interacting directly with the operating system.

Examples:

```python
import os

os.getenv("HOME")
os.getcwd()
os.chdir("documents")
```

## Common Conclusion

Modern Python code often combines both modules:

```python
from pathlib import Path
import os
```

Use:

- `pathlib` for file system paths;
- `os` for operating system interactions.

## Summary

### Path Operations

```python
Path(...)
Path.exists()
Path.is_file()
Path.is_dir()
```

### Operating System Operations

```python
os.getenv()
os.environ
os.getcwd()
os.chdir()
os.listdir()
```

## Status

✅ Completed