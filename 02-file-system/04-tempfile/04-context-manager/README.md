# Context Managers

The `with` statement is commonly used with `tempfile` to manage temporary resources safely.

A context manager automatically handles resource cleanup when execution leaves the `with` block, even if an error occurs.

Using `with` helps write safer, cleaner, and more reliable code.

## Learning Objectives

After completing this chapter, I should be able to:

- Understand the purpose of `with`.
- Use context managers with temporary files.
- Use context managers with temporary directories.
- Understand automatic cleanup.
- Understand the role of `as`.
- Know why context managers are safer than manual cleanup.

---

## Topics Covered

- with
- as
- TemporaryFile()
- NamedTemporaryFile()
- TemporaryDirectory()
- Automatic cleanup
- Resource management

---

## The with Statement

A context manager follows this workflow:

```text
Enter block
↓
Create resource
↓
Use resource
↓
Leave block
↓
Automatic cleanup
```

---

## The as Keyword

The `as` keyword stores the created resource in a variable.

Example:

```python
with ... as resource:
```

```text
resource
↓
usable inside the block
```

---

## Temporary Files

Example workflow:

```text
with TemporaryFile()
↓
write
↓
read
↓
automatic cleanup
```

---

## Temporary Directories

Example workflow:

```text
with TemporaryDirectory()
↓
create files
↓
create folders
↓
automatic cleanup
```

---

## Why Use Context Managers?

Without `with`:

```text
Create
↓
Use
↓
Remember to close
↓
Remember to clean up
```

With `with`:

```text
Create
↓
Use
↓
Automatic cleanup
```

---

## Error Handling

Even if an error occurs:

```text
Create resource
↓
Error
↓
Exit block
↓
Cleanup still happens
```

This is one of the main advantages of context managers.

---

## Typical Use Cases

### Files

```text
Open file
↓
Read or write
↓
Close automatically
```

### Temporary Resources

```text
Create temporary file
↓
Process data
↓
Delete automatically
```

### Testing

```text
Create test environment
↓
Run tests
↓
Cleanup
```

---

## Summary

```text
with
↓
context manager

as
↓
resource variable

TemporaryFile()
↓
temporary file

TemporaryDirectory()
↓
temporary directory

automatic cleanup
↓
main benefit
```

---

## Status

✅ Completed