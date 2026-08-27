# Temporary Directories

The `tempfile` module can create temporary directories using `TemporaryDirectory()`.

A temporary directory provides an isolated workspace where files and subdirectories can be created safely during program execution.

When the temporary directory is no longer needed, it is automatically removed along with all of its contents.

## Learning Objectives

After completing this chapter, I should be able to:

- Create temporary directories.
- Access the temporary directory path.
- Use `Path()` with temporary directories.
- Create files inside a temporary directory.
- Create subdirectories inside a temporary directory.
- Explore directory contents.
- Understand automatic cleanup.

---

## Topics Covered

- TemporaryDirectory()
- Directory paths
- Path()
- Creating files
- Creating directories
- Exploring contents
- Automatic cleanup

---

## TemporaryDirectory()

Creates a temporary directory.

```python
tempfile.TemporaryDirectory()
```

---

## Accessing the Path

The directory path is available through:

```python
temp_dir.name
```

Example:

```text
/tmp/tmpyq9xysyx
```

---

## Using Path()

The path can be converted into a `Path` object:

```python
Path(temp_dir.name)
```

This makes file and directory manipulation easier.

---

## Creating Files

Example workflow:

```text
TemporaryDirectory
↓
notes.txt
```

---

## Creating Directories

Example workflow:

```text
TemporaryDirectory
↓
data/
```

---

## Exploring Contents

Directory contents can be listed with:

```python
path.iterdir()
```

---

## Automatic Cleanup

```text
Create directory
↓
Use directory
↓
Directory removed automatically
```

All files and subdirectories inside the temporary directory are removed as well.

---

## Typical Use Cases

### Testing

```text
Create test environment
↓
Run tests
↓
Cleanup
```

### ZIP Extraction

```text
Archive
↓
Temporary directory
↓
Processing
↓
Cleanup
```

### Report Generation

```text
Temporary files
↓
Final report
↓
Cleanup
```

---

## Summary

```text
TemporaryDirectory()
↓
temporary directory

name
↓
directory path

Path(...)
↓
path manipulation

iterdir()
↓
list contents

automatic cleanup
↓
main advantage
```

---

## Status

✅ Completed