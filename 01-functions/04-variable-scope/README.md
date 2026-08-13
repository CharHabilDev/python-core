# Variable Scope

## Introduction

Variable scope determines where a variable can be accessed in a program.

Understanding scope is essential for writing predictable and maintainable code.

Python mainly works with:

- local variables;
- global variables.

---

## Local Variables

A variable created inside a function is called a local variable.

```python
def saluer():
    nom = "Ali"
    print(nom)
```

Calling the function:

```python
saluer()
```

Output:

```text
Ali
```

Trying to access the variable outside the function results in an error:

```python
print(nom)
```

Output:

```text
NameError: name 'nom' is not defined
```

The variable only exists inside the function.

---

## Global Variables

A variable defined outside a function is called a global variable.

```python
ville = "Cotonou"

def afficher_ville():
    print(ville)
```

Calling the function:

```python
afficher_ville()
```

Output:

```text
Cotonou
```

Functions can read global variables.

---

## Local Variables and Global Variables

A local variable can have the same name as a global variable.

```python
nom = "Ali"

def afficher():
    nom = "Fatima"
    print(nom)

afficher()
print(nom)
```

Output:

```text
Fatima
Ali
```

The local variable hides the global variable inside the function.

---

## The global Keyword

By default, assigning a value inside a function creates a local variable.

```python
compteur = 0

def incrementer():
    compteur += 1
```

This produces an error because Python treats `compteur` as a local variable.

To modify a global variable, use the `global` keyword.

```python
compteur = 0

def incrementer():
    global compteur
    compteur += 1
```

Example:

```python
incrementer()
incrementer()
incrementer()

print(compteur)
```

Output:

```text
3
```

---

## Function Parameters

Function parameters are local variables.

```python
def afficher(nom):
    print(nom)
```

Here, `nom` only exists while the function is executing.

After the function ends, the parameter disappears.

---

## Why Avoid Global Variables?

Global variables can:

- make code harder to understand;
- create unexpected side effects;
- complicate testing and debugging.

A better approach is often to pass values as parameters and return results.

```python
def incrementer(compteur):
    return compteur + 1
```

Example:

```python
compteur = incrementer(compteur)
```

This approach is easier to maintain and test.

---

## Best Practices

✅ Prefer local variables.

✅ Pass data through parameters.

✅ Return values using `return`.

✅ Keep functions independent when possible.

❌ Avoid excessive use of global variables.

---

## Key Takeaways

- Local variables only exist inside a function.
- Global variables exist throughout the program.
- Local variables can hide global variables with the same name.
- The `global` keyword allows modification of a global variable.
- Function parameters are local variables.
- Prefer parameters and return values over global variables.