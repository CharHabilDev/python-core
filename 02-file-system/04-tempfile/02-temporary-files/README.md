# Temporary Files

The `tempfile` module provides tools for creating temporary files safely.

Temporary files can be used like regular files, but they are automatically removed when they are no longer needed.

This makes them useful for testing, data processing, file conversion, and intermediate storage.

## Learning Objectives

After completing this chapter, I should be able to:

- Create temporary files.
- Write data to temporary files.
- Read data from temporary files.
- Understand the role of `seek(0)`.
- Use `TemporaryFile()`.
- Use `NamedTemporaryFile()`.
- Understand when a visible filename is required.

---

## Topics Covered

- TemporaryFile()
- NamedTemporaryFile()
- Writing data
- Reading data
- File cursor
- seek(0)
- Visible filenames

---

## TemporaryFile()

Creates a temporary file.

```python
tempfile.TemporaryFile()
```

Characteristics:

```text
temporary file
↓
automatic cleanup
↓
generally no usable filename
```

---

## NamedTemporaryFile()

Creates a temporary file with a visible filename.

```python
tempfile.NamedTemporaryFile()
```

Characteristics:

```text
temporary file
↓
automatic cleanup
↓
visible filename
```

---

## Writing Data

Temporary files support writing operations.

```text
write()
↓
store data
```

---

## Reading Data

Temporary files support reading operations.

```text
read()
↓
retrieve data
```

---

## File Cursor

After writing:

```text
Bonjour tempfile
                ↑
             cursor
```

Reading immediately may return nothing because the cursor is already at the end of the file.

---

## seek(0)

Returns the cursor to the beginning.

```python
temp.seek(0)
```

```text
Bonjour tempfile
↑
start
```

This allows the content to be read again.

---

## The name Attribute

With:

```python
temp.name
```

Python returns the temporary file path.

Example:

```text
/tmp/tmpabcd123
```

The exact value depends on the operating system.

---

## When to Use NamedTemporaryFile()

Useful when another library requires:

```text
a real filename
↓
a filesystem path
```

instead of only a file object.

---

## Typical Use Cases

### Testing

```text
Create temporary file
↓
Run tests
↓
Automatic cleanup
```

### Data Processing

```text
Download
↓
Temporary file
↓
Process data
↓
Delete file
```

### File Conversion

```text
Input file
↓
Temporary file
↓
Output file
```

---

## Summary

```text
TemporaryFile()
↓
temporary file

NamedTemporaryFile()
↓
temporary file with visible filename

write()
↓
write data

read()
↓
read data

seek(0)
↓
return cursor to beginning

name
↓
temporary file path
```

---

## Status

✅ Completed