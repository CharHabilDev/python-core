# Archives

The `shutil` module can create and extract archives.

Archives are commonly used for backups, file transfers, deployments, and data storage.

The most common format is ZIP.

## Learning Objectives

After completing this chapter, I should be able to:

- Create ZIP archives.
- Extract archives.
- Use `shutil.make_archive()`.
- Use `shutil.unpack_archive()`.
- Verify archive creation.
- Understand common archive use cases.

---

## Topics Covered

- Archive creation
- Archive extraction
- ZIP format
- Archive verification
- Backup workflows
- Data recovery

---

## Key Concepts

### Creating an Archive

`make_archive()` creates a compressed archive from a directory.

Example:

```python
shutil.make_archive(
    "project_backup",
    "zip",
    "project"
)
```

Result:

```text
project/
↓
project_backup.zip
```

---

### Archive Formats

Common formats:

| Format | Description        |
| ------ | ------------------ |
| zip    | Most common format |
| tar    | Common on Linux    |
| gztar  | tar.gz             |
| bztar  | tar.bz2            |
| xztar  | tar.xz             |

For most projects:

```text
zip
```

is sufficient.

---

### Verifying an Archive

An archive is a normal file.

Example:

```python
Path("project_backup.zip").exists()
```

---

### Extracting an Archive

`unpack_archive()` extracts files from an archive.

Example:

```python
shutil.unpack_archive(
    archive_path,
    destination
)
```

Result:

```text
project_backup.zip
↓
restored_project/
```

---

### Archive Recovery

An archive can serve as a backup.

Example:

```text
project/
↓ deleted

project_backup.zip
↓ still available

restore possible
```

---

## pathlib + shutil

A common pattern:

```python
from pathlib import Path
import shutil

root = Path("sandbox")

shutil.make_archive(
    root / "backup",
    "zip",
    root / "project"
)
```

`Path` handles paths.

`shutil` creates and extracts archives.

---

## Real-World Use Cases

- Project backups
- Log archiving
- Data exports
- File transfers
- Deployment packages
- Historical data storage

---

## Comparison

| Function           | Purpose                 |
| ------------------ | ----------------------- |
| `make_archive()`   | Create an archive       |
| `unpack_archive()` | Extract an archive      |
| `copytree()`       | Copy a directory        |
| `rmtree()`         | Remove a directory tree |

---

## Summary

```text
make_archive()
↓
create archive

unpack_archive()
↓
extract archive

zip
↓
most common format

archive
↓
backup and transfer solution
```

---

## Status

✅ Completed