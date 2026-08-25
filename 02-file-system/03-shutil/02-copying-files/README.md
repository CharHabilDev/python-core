# Copying Files

The `shutil` module provides simple and efficient ways to copy files.

It is commonly used for backups, file exports, data duplication, and deployment tasks.

## Learning Objectives

After completing this chapter, I should be able to:

- Copy a file using `shutil.copy()`.
- Copy a file using `shutil.copy2()`.
- Understand the difference between `copy()` and `copy2()`.
- Copy files into another directory.
- Combine `pathlib` and `shutil` effectively.
- Verify that copied files exist and contain the expected data.

---

## Topics Covered

- `shutil.copy()`
- `shutil.copy2()`
- Copying to another file
- Copying to another directory
- File verification
- Copying metadata

---

## Key Concepts

### `shutil.copy()`

Copies a file and its content to a new location.

```python
shutil.copy(source, destination)
```

---

### `shutil.copy2()`

Copies a file and preserves additional metadata such as modification times.

```python
shutil.copy2(source, destination)
```

---

### `pathlib` + `shutil`

A common pattern:

```python
source = Path(...)
destination = Path(...)

shutil.copy(source, destination)
```

`Path` builds paths.

`shutil` performs the file operation.

---

## Comparison

| Function  | File Content | Metadata   |
| --------- | ------------ | ---------- |
| `copy()`  | ✅           | ⚠️ Partial |
| `copy2()` | ✅           | ✅         |

---

## Real-World Use Cases

- Automatic backups
- Exporting reports
- Duplicating configuration files
- Preparing deployment files
- Creating restore points

---

## Summary

```text
copy()
↓
copies file content

copy2()
↓
copies file content
+
preserves more metadata

Path
↓
builds paths

shutil
↓
copies files
```

---

## Status

✅ Completed