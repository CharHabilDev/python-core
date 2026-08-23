# Files and Directories

This chapter introduces basic file and directory manipulation using the `pathlib` module.

It focuses on creating and deleting files and folders while understanding common filesystem behaviors and errors.

## Learning Objectives

After completing this chapter, I should be able to:

- Create files with `touch()`.
- Create directories with `mkdir()`.
- Create nested directory structures.
- Use `exist_ok=True` safely.
- Delete files with `unlink()`.
- Delete empty directories with `rmdir()`.
- Understand common filesystem exceptions.

## Topics Covered

- `touch()`
- `mkdir()`
- `exist_ok=True`
- `parents=True`
- `unlink()`
- `missing_ok=True`
- `rmdir()`

## Key Concepts

### Creating a File

```python
Path("notes.txt").touch()
```

Creates the file if it does not already exist.

### Creating a Directory

```python
Path("documents").mkdir()
```

Creates a new directory.

### Creating Parent Directories

```python
Path("cours/python/pathlib").mkdir(
    parents=True,
    exist_ok=True
)
```

Creates all missing parent directories automatically.

### Removing a File

```python
Path("notes.txt").unlink()
```

Deletes a file.

### Removing an Empty Directory

```python
Path("documents").rmdir()
```

Deletes a directory only if it is empty.

### Safe File Removal

```python
Path("notes.txt").unlink(
    missing_ok=True
)
```

Avoids raising an exception if the file does not exist.

## Common Errors

### FileExistsError

Raised when attempting to create a directory that already exists.

### FileNotFoundError

Raised when attempting to remove a file that does not exist.

### OSError

Raised when attempting to remove a directory that is not empty.

## Status

✅ Completed