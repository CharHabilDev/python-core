# shutil vs os vs pathlib

Python provides several modules for working with files, directories, and the operating system.

Although they sometimes overlap, each module has a specific role.

Understanding when to use each one helps write cleaner and more maintainable code.

## Learning Objectives

After completing this chapter, I should be able to:

- Distinguish between `pathlib`, `os`, and `shutil`.
- Choose the appropriate module for a task.
- Combine multiple modules in real-world scripts.
- Understand modern Python file-system practices.

---

## Topics Covered

- `pathlib`
- `os`
- `shutil`
- Module responsibilities
- Real-world workflows
- Best practices

---

## pathlib

`pathlib` is specialized in path manipulation.

Typical uses:

- Build paths
- Navigate directories
- Check file existence
- Check directory existence
- Manipulate file names and extensions

Examples:

```python
Path("documents") / "notes.txt"

path.exists()

path.is_file()

path.is_dir()
```

---

## os

`os` provides access to operating system features.

Typical uses:

- Get the current working directory
- Change directory
- Read environment variables
- Access operating system information

Examples:

```python
os.getcwd()

os.chdir()

os.getenv()

os.environ
```

---

## shutil

`shutil` provides high-level file and directory operations.

Typical uses:

- Copy files
- Copy directories
- Move files
- Move directories
- Create archives
- Extract archives
- Remove directory trees

Examples:

```python
shutil.copy()

shutil.copytree()

shutil.move()

shutil.make_archive()

shutil.unpack_archive()

shutil.rmtree()
```

---

## Responsibilities

| Module    | Main Responsibility          |
| --------- | ---------------------------- |
| `pathlib` | Path management              |
| `os`      | Operating system interaction |
| `shutil`  | High-level file operations   |

---

## Comparison

| Task                       | Recommended Module |
| -------------------------- | ------------------ |
| Build a path               | `pathlib`          |
| Verify file existence      | `pathlib`          |
| Verify directory existence | `pathlib`          |
| Read environment variables | `os`               |
| Get current directory      | `os`               |
| Copy a file                | `shutil`           |
| Copy a directory           | `shutil`           |
| Move files                 | `shutil`           |
| Create ZIP archives        | `shutil`           |
| Delete a directory tree    | `shutil`           |

---

## Typical Workflow

A backup script may use all three modules:

```text
os
↓
read configuration

pathlib
↓
build and validate paths

shutil
↓
copy and archive data
```

---

## Modern Python Recommendation

Most modern Python projects use:

```text
pathlib
+
shutil
```

for file-system operations.

`os` remains essential for operating-system features such as:

- Environment variables
- Working directories
- System information

---

## Summary

```text
pathlib
↓
paths

os
↓
operating system

shutil
↓
high-level file operations
```

---

## Status

✅ Completed