# Moving and Renaming

The `shutil` module provides the `move()` function, which can move files and directories or rename them.

Unlike copying operations, moving transfers the original item to a new location instead of creating a duplicate.

## Learning Objectives

After completing this chapter, I should be able to:

- Move files using `shutil.move()`.
- Move directories using `shutil.move()`.
- Rename files and directories.
- Verify that a move operation completed successfully.
- Understand the difference between copying and moving.
- Use `pathlib` and `shutil` together.

---

## Topics Covered

- Moving files
- Moving directories
- Renaming files
- Renaming directories
- Verifying move operations
- Common real-world use cases

---

## Key Concepts

### Moving a File

A file can be moved from one directory to another.

```python
shutil.move(source, destination)
```

Example:

```text
files/notes.txt
↓
archives/notes.txt
```

---

### Renaming a File

A file can be renamed by moving it to a new name.

```python
shutil.move(
    "report.txt",
    "annual_report.txt"
)
```

Result:

```text
report.txt
↓
annual_report.txt
```

---

### Moving a Directory

Entire directory trees can be moved.

```python
shutil.move(
    source_directory,
    destination_directory
)
```

All files and subdirectories are moved together.

---

### Verifying a Move

After moving:

```text
source
↓
does not exist

destination
↓
exists
```

It is good practice to verify both conditions.

---

## Comparison

| Function  | Result                                          |
| --------- | ----------------------------------------------- |
| `copy()`  | Creates a duplicate                             |
| `copy2()` | Creates a duplicate and preserves more metadata |
| `move()`  | Transfers the original item                     |

---

## pathlib + shutil

A common pattern:

```python
source = Path(...)
destination = Path(...)

shutil.move(
    source,
    destination
)
```

`Path` builds paths.

`shutil` performs the operation.

---

## Real-World Use Cases

* Automatic file organization
* Log rotation
* Archiving old reports
* Data migration
* File processing pipelines

---

## Summary

```text
copy()
↓
duplicate

copy2()
↓
duplicate + metadata

move()
↓
move original item

move()
↓
can also rename files and directories
```

---

## Status

✅ Completed
