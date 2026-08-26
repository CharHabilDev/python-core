# Copying Directories

The `shutil` module can copy entire directory trees using `shutil.copytree()`.

Unlike `copy()` and `copy2()`, which work on individual files, `copytree()` duplicates a directory, its subdirectories, and all contained files.

## Learning Objectives

After completing this chapter, I should be able to:

- Copy an entire directory tree.
- Use `shutil.copytree()`.
- Understand why the destination must not exist by default.
- Use `dirs_exist_ok=True` when appropriate.
- Verify that directories and files were copied correctly.
- Understand common use cases for directory duplication.

---

## Topics Covered

- `shutil.copytree()`
- Recursive directory copying
- Existing destination directories
- `dirs_exist_ok=True`
- Verifying copied data
- Directory backups

---

## Key Concepts

### Copying a Directory

`copytree()` copies:

```text
✓ folders
✓ subfolders
✓ files
✓ complete structure
````

Example:

```python
shutil.copytree(source, destination)
```

---

### Existing Destination

By default:

```python
shutil.copytree(source, destination)
```

raises:

```text
FileExistsError
```

if the destination directory already exists.

This behavior helps prevent accidental overwriting of data.

---

### Allow Existing Destination

Since Python 3.8:

```python
shutil.copytree(
    source,
    destination,
    dirs_exist_ok=True
)
```

allows copying into an existing directory.

Important:

```text
dirs_exist_ok=True
≠
delete destination first
```

Python does not remove the destination directory.

Instead, it copies files into it and may replace files that have the same name.

---

### pathlib + shutil

A common pattern:

```python
source = Path(...)
destination = Path(...)

shutil.copytree(
    source,
    destination
)
```

`Path` manages paths.

`shutil` performs the copy operation.

---

## Comparison

| Function     | Purpose                                  |
| ------------ | ---------------------------------------- |
| `copy()`     | Copy one file                            |
| `copy2()`    | Copy one file and preserve more metadata |
| `copytree()` | Copy an entire directory tree            |

---

## Real-World Use Cases

- Project backups
- Dataset duplication
- Deployment preparation
- File synchronization
- Testing environments

---

## Summary

```text
copy()
↓
one file

copy2()
↓
one file + metadata

copytree()
↓
entire directory tree

dirs_exist_ok=False
↓
error if destination exists

dirs_exist_ok=True
↓
allow copy into existing directory
```

---

## Status

✅ Completed