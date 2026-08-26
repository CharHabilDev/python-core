# Removing Directory Trees

The `shutil` module provides the `rmtree()` function, which removes an entire directory tree.

Unlike `Path.rmdir()`, which only removes empty directories, `rmtree()` removes a directory and everything inside it.

## Learning Objectives

After completing this chapter, I should be able to:

- Remove a complete directory tree.
- Use `shutil.rmtree()`.
- Understand the difference between `rmdir()` and `rmtree()`.
- Verify that a directory exists before deleting it.
- Apply basic safety checks before destructive operations.
- Identify common use cases for recursive deletion.

---

## Topics Covered

- Recursive directory deletion
- `shutil.rmtree()`
- `Path.rmdir()`
- Safety checks
- Directory existence verification
- Cleanup operations

---

## Key Concepts

### Removing an Empty Directory

`Path.rmdir()` only works when the directory contains no files or subdirectories.

```python
Path("empty_folder").rmdir()
```

If the directory is not empty, Python raises an exception.

---

### Removing a Directory Tree

`shutil.rmtree()` removes:

```text
✓ directory
✓ subdirectories
✓ files
✓ complete tree
```

Example:

```python
shutil.rmtree(path)
```

---

### Difference Between rmdir() and rmtree()

| Function   | Empty Directory | Non-Empty Directory |
| ---------- | :-------------: | :-----------------: |
| `rmdir()`  |        ✅       |          ❌         |
| `rmtree()` |        ✅       |          ✅         |

---

### Safety Checks

Before deleting a directory, it is often useful to verify:

```python
path.exists()
```

and

```python
path.is_dir()
```

Example:

```python
if path.exists() and path.is_dir():
    shutil.rmtree(path)
```

This helps avoid deleting the wrong target.

---

### Common Pattern

```python
from pathlib import Path
import shutil

path = Path("sandbox/project")

if path.exists() and path.is_dir():
    shutil.rmtree(path)
```

---

## Real-World Use Cases

- Cleaning temporary directories
- Removing cache folders
- Resetting development environments
- Cleaning test data
- Deleting generated files

---

## Comparison

| Function   | Purpose                                 |
| ---------- | --------------------------------------- |
| `unlink()` | Remove a file                           |
| `rmdir()`  | Remove an empty directory               |
| `rmtree()` | Remove a directory and all its contents |

---

## Summary

```text
unlink()
↓
remove file

rmdir()
↓
remove empty directory

rmtree()
↓
remove directory tree

exists() + is_dir()
↓
recommended safety checks
```

---

## Status

✅ Completed