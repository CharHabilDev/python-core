# Properties and Navigation

This chapter focuses on inspecting and navigating file system paths with `pathlib`.

It introduces useful properties and methods for retrieving information about files and directories.

## Learning Objectives

After completing this chapter, I should be able to:

- Retrieve a file or directory name.
- Extract file extensions.
- Access parent directories.
- Break a path into its components.
- Check whether a path exists.
- Determine whether a path is a file or a directory.

## Topics Covered

- `.name`
- `.stem`
- `.suffix`
- `.parent`
- `.parts`
- `.exists()`
- `.is_file()`
- `.is_dir()`

## Key Concepts

### File Name

```python
Path("documents/notes.txt").name
````

Returns:

```text
notes.txt
```

### File Stem

```python
Path("documents/notes.txt").stem
```

Returns:

```text
notes
```

### File Extension

```python
Path("documents/notes.txt").suffix
```

Returns:

```text
.txt
```

### Parent Directory

```python
Path("documents/notes.txt").parent
```

Returns:

```text
documents
```

### Path Components

```python
Path("documents/python/notes.txt").parts
```

Returns:

```python
('documents', 'python', 'notes.txt')
```

### Path Existence

```python
Path("README.md").exists()
```

Returns `True` or `False`.

### File and Directory Checks

```python
Path("README.md").is_file()
Path("documents").is_dir()
```

Return `True` or `False`.

## Status

✅ Completed