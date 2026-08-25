# Environment Variables

This chapter introduces environment variables and how Python applications can access external configuration using the `os` module.

Environment variables are commonly used to store configuration values, API keys, database credentials, and application settings without hardcoding them into source code.

## Learning Objectives

After completing this chapter, I should be able to:

- Understand what environment variables are.
- Read environment variables using `os.getenv()`.
- Use default values when variables are missing.
- Access environment variables through `os.environ`.
- Check whether a variable exists.
- Understand why environment variables are commonly used in real-world projects.

## Topics Covered

- `os.getenv()`
- `os.environ`
- `os.environ.items()`
- Default values
- Environment variable existence checks

## Key Concepts

### Reading an Environment Variable

```python
import os

home = os.getenv("HOME")
print(home)
```

Returns the value of the environment variable if it exists.

### Using a Default Value

```python
import os

database_url = os.getenv(
    "DATABASE_URL",
    "sqlite.db"
)
```

Returns `"sqlite.db"` if the variable does not exist.

### Accessing Variables with os.environ

```python
import os

user = os.environ["USER"]
print(user)
```

Raises a `KeyError` if the variable is missing.

### Listing Environment Variables

```python
import os

for key, value in os.environ.items():
    print(key, value)
```

Displays all available environment variables.

### Checking Existence

```python
import os

if "HOME" in os.environ:
    print("Exists")
```

Checks whether a variable is available.

## getenv() vs environ[]

| Feature                   | `os.getenv()`  | `os.environ[]`    |
| ------------------------- | -------------- | ----------------- |
| Missing variable          | Returns `None` | Raises `KeyError` |
| Default value support     | ✅ Yes          | ❌ No              |
| Safer for optional values | ✅              | ❌                 |

## Common Use Cases

- API keys
- Database credentials
- Application configuration
- Development and production settings
- CI/CD pipelines
- Docker containers

## Why Use Environment Variables?

Instead of writing:

```python
API_KEY = "my-secret-key"
```

applications often use:

```python
import os

API_KEY = os.getenv("API_KEY")
```

This keeps sensitive information outside the source code and reduces the risk of exposing secrets.

## Status

✅ Completed