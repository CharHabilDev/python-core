# System Information

This chapter introduces the `platform` module and how Python can retrieve information about the operating system, machine architecture, and Python runtime environment.

These tools are commonly used for diagnostics, debugging, compatibility checks, and system reports.

## Learning Objectives

After completing this chapter, I should be able to:

- Retrieve information about the operating system.
- Identify the system version.
- Inspect machine architecture.
- Determine the Python version in use.
- Identify the Python interpreter.
- Generate simple system reports.
- Understand the difference between `os` and `platform`.

## Topics Covered

- `platform.system()`
- `platform.release()`
- `platform.platform()`
- `platform.machine()`
- `platform.python_version()`
- `platform.python_implementation()`

## Key Concepts

### Operating System Name

```python
import platform

print(platform.system())
```

Examples:

```text
Linux
Windows
Darwin
```

Note:
```txt
Darwin = macOS
```

---

### Operating System Release

```python
import platform

print(platform.release())
```

Examples:

```text
6.8.0-64-generic
11
```

---

### Detailed Platform Information

```python
import platform

print(platform.platform())
```

Example:

```text
Linux-6.8.0-64-generic-x86_64-with-glibc2.39
```

---

### Machine Architecture

```python
import platform

print(platform.machine())
```

Examples:

```text
x86_64
AMD64
arm64
aarch64
```

---

### Python Version

```python
import platform

print(platform.python_version())
```

Example:

```text
3.12.10
```

---

### Python Implementation

```python
import platform

print(platform.python_implementation())
```

Examples:

```text
CPython
PyPy
Jython
IronPython
```

## Common Use Cases

- Environment diagnostics.
- Debugging compatibility issues.
- Installation scripts.
- System reports.
- Cross-platform applications.

## platform vs os

| Feature                    | `os`    | `platform` |
| -------------------------- | ------- | ---------- |
| File system operations     | ✅      | ❌         |
| Environment variables      | ✅      | ❌         |
| Working directory          | ✅      | ❌         |
| System identification      | Limited | ✅         |
| Python runtime information | ❌      | ✅         |

### Example

```python
import os
import platform

print(os.name)
print(platform.system())
```

Output on Linux:

```text
posix
Linux
```

Output on Windows:

```text
nt
Windows
```

`os.name` identifies the operating system family, while `platform.system()` provides the actual operating system name.

## Mini Example

```python
import platform

print("=== SYSTEM REPORT ===")

print(f"System      : {platform.system()}")
print(f"Release     : {platform.release()}")
print(f"Machine     : {platform.machine()}")
print(f"Python      : {platform.python_version()}")
print(f"Interpreter : {platform.python_implementation()}")
```

## Status

✅ Completed