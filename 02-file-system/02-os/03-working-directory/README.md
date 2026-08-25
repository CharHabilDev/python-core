# Working Directory

This chapter introduces the concept of the Current Working Directory (CWD) and how Python programs can navigate between directories using the `os` module.

Understanding the working directory is essential because many file operations depend on the location from which a program is executed.

## Learning Objectives

After completing this chapter, I should be able to:

- Retrieve the current working directory.
- Change the current working directory.
- Understand how file operations depend on the current location.
- Navigate between directories safely.
- Restore the original working directory after changes.
- Avoid common `FileNotFoundError` issues related to incorrect paths.

## Topics Covered

- `os.getcwd()`
- `os.chdir()`
- `os.listdir()`
- Current Working Directory (CWD)

## Key Concepts

### Get Current Working Directory

```python
import os

print(os.getcwd())
```

Returns the absolute path of the current working directory.

### Change Directory

```python
import os

os.chdir("documents")
```

Changes the current working directory.

### Save Current Directory

```python
import os

original_directory = os.getcwd()
```

Stores the current location before navigating elsewhere.

### Return to Previous Directory

```python
import os

os.chdir(original_directory)
```

Returns to the previously saved location.

### List Directory Contents

```python
import os

print(os.listdir())
```

Displays the contents of the current working directory.

## Why the Working Directory Matters

Many operations use relative paths:

```python
open("data.txt")
```

Python will search for `data.txt` in the current working directory.

If the file is not located there, Python raises:

```text
FileNotFoundError
```

even if the file exists elsewhere on the system.

## Common Use Cases

- Navigating project folders.
- Processing files in different directories.
- Running automation scripts.
- Managing backups.
- Debugging path-related errors.

## Common Mistakes

### Forgetting the Current Directory

```python
os.chdir("data")
```

Later:

```python
open("config.json")
```

Python now searches inside:

```text
data/config.json
```

which may not be the intended location.

### Not Restoring the Original Directory

When changing directories temporarily, it is often useful to save the original location and restore it when finished.

## Status

✅ Completed