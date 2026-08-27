# tempfile vs Manual Files

The `tempfile` module provides a safer and more convenient way to work with temporary files and directories than creating them manually.

Instead of choosing names, handling cleanup, and managing errors yourself, `tempfile` automatically creates unique temporary resources and removes them when they are no longer needed.

## Learning Objectives

After completing this chapter, I should be able to:

- Compare manual files and temporary files.
- Understand the risks of manual temporary file management.
- Explain the advantages of `tempfile`.
- Know when to use `tempfile`.
- Know when a regular file is more appropriate.

---

## Topics Covered

- Manual temporary files
- Temporary files
- Unique filenames
- Automatic cleanup
- Error handling
- Temporary vs permanent data

---

## Manual File Approach

Example:

```python
Path("temp.txt")
```

Workflow:

```text
Create
↓
Use
↓
Delete manually
```

---

## Risks of Manual Files

### Name Collisions

```text
temp.txt
↓
already exists
↓
conflict
```

### Forgotten Cleanup

```text
Create
↓
Use
↓
Program ends
↓
file remains
```

### Runtime Errors

```text
Create
↓
Error
↓
Program stops
↓
cleanup skipped
```

---

## tempfile Approach

Workflow:

```text
Create
↓
Unique name
↓
Use
↓
Automatic cleanup
```

---

## Comparison

| Feature                   | Manual File | tempfile |
| ------------------------- | ----------- | -------- |
| Unique filename           | ❌          | ✅        |
| Automatic cleanup         | ❌          | ✅        |
| Error safety              | ❌          | ✅        |
| Temporary data management | ❌          | ✅        |
| Convenience               | ❌          | ✅        |

---

## When to Use tempfile

### Temporary Downloads

```text
Download
↓
Process
↓
Delete
```

### Data Processing

```text
Input
↓
Temporary workspace
↓
Output
```

### Automated Testing

```text
Create environment
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
Analysis
↓
Cleanup
```

---

## When Not to Use tempfile

### Permanent Files

```text
users.db
config.json
report.pdf
```

### Long-Term Storage

```text
Photos
Documents
Backups
```

These files must remain available after program execution.

---

## Summary

```text
tempfile
↓
temporary data

Path()
↓
permanent data

tempfile
↓
unique names

tempfile
↓
automatic cleanup

manual files
↓
full control
```

---

## Status

✅ Completed