# Introduction

The `shutil` module provides high-level operations on files and directories.

While `pathlib` focuses on path manipulation and `os` interacts with the operating system, `shutil` is designed to perform common file management tasks such as copying, moving, archiving, and removing files or directories.

## Learning Objectives

After completing this chapter, I should be able to:

- Understand the purpose of the `shutil` module.
- Identify common file operations supported by `shutil`.
- Understand the difference between `pathlib`, `os`, and `shutil`.
- Know when to use each module.
- Recognize real-world use cases for `shutil`.

---

## Topics Covered

- What is `shutil`?
- High-level file operations
- Copying files
- Moving files and directories
- Removing directory trees
- Creating archives
- `pathlib` vs `os` vs `shutil`

---

## Key Concepts

### pathlib

Used to create and manipulate file system paths.

Examples:

```python
from pathlib import Path

path = Path("documents") / "notes.txt"
```

### os

Used to interact with the operating system.

Examples:

```python
import os

os.getcwd()
os.getenv("HOME")
```

### shutil

Used to perform high-level operations on files and directories.

Examples:

```python
import shutil

shutil.copy(...)
shutil.move(...)
shutil.rmtree(...)
```

---

## Comparison

| Module  | Main Purpose                             |
| ------- | ---------------------------------------- |
| pathlib | Path manipulation                        |
| os      | Operating system interaction             |
| shutil  | High-level file and directory operations |

---

## Summary

```text
pathlib
↓
Build and manipulate paths

os
↓
Interact with the operating system

shutil
↓
Copy, move, archive and remove files or directories
```

---

## Status

✅ Completed