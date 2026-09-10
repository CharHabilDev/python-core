# Creating a defaultdict

## Summary

### Default Factory

A factory creates the default value for missing keys.

### Common Factories

| Factory | Default Value |
|----------|----------|
| int | 0 |
| list | [] |
| set | set() |
| str | "" |

### Workflow

Missing key
↓
Factory
↓
Default value

### Common Uses

- Counting
- Grouping
- Categorization