# Accessing Counts

## Summary

### Accessing Values

Counter values are accessed using keys.

```python
counter["apple"]
```

### Missing Keys

Missing keys return:

```text
0
```

instead of raising an error.

### Iteration

```python
counter.items()
```

returns:

```text
element → count
```

### Common Use Cases

- Text analysis
- Vote counting
- Log analysis
- Sales statistics