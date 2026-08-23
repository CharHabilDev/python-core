# Directory Traversal

This chapter focuses on exploring directory contents and searching for files using `pathlib`.

It introduces techniques for traversing folders, filtering results, and performing recursive searches through an entire directory tree.

## Learning Objectives

After completing this chapter, I should be able to:

- List the contents of a directory.
- Distinguish files from directories.
- Search for files using patterns.
- Perform recursive searches in subdirectories.
- Understand the difference between `glob()` and `rglob()`.
- Build simple filesystem exploration tools.

## Topics Covered

- `iterdir()`
- `glob()`
- `rglob()`
- `is_file()`
- `is_dir()`

## Key Concepts

### Listing Directory Contents

```python
from pathlib import Path

for item in Path("documents").iterdir():
    print(item)
```

Lists all items directly inside the directory.

### Filtering Files

```python
for item in Path("documents").iterdir():
    if item.is_file():
        print(item)
```

Displays only files.

### Filtering Directories

```python
for item in Path("documents").iterdir():
    if item.is_dir():
        print(item)
```

Displays only directories.

### Searching with glob()

```python
Path("documents").glob("*.txt")
```

Searches for all `.txt` files in the current directory only.

### Recursive Search with rglob()

```python
Path("documents").rglob("*.txt")
```

Searches for all `.txt` files in the directory and all subdirectories.

## Pattern Examples

### All Text Files

```python
Path("documents").glob("*.txt")
```

### All Python Files

```python
Path("project").rglob("*.py")
```

### Everything

```python
Path("documents").glob("*")
```

## Common Use Cases

- Searching configuration files.
- Finding Python modules in a project.
- Locating logs.
- Building backup scripts.
- Exploring unknown directory structures.

## Status

✅ Completed