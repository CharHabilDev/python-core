# Exercices

### Exercice 1

Importe `os`.

Affiche :

```python
os.getenv("HOME")
```

---

### Exercice 2

Affiche :

```python
os.getenv("USER")
```

ou

```python
os.getenv("USERNAME")
```

selon ton système.

---

### Exercice 3

Affiche une variable inexistante :

```python
os.getenv("VARIABLE_INVENTEE")
```

Observe le résultat.

---

### Exercice 4

Utilise :

```python
os.getenv(
    "VARIABLE_INVENTEE",
    "valeur_par_defaut"
)
```

Observe le résultat.

---

### Exercice 5

Affiche les 10 premières variables d'environnement.

Indice conceptuel :

```text
os.environ
↓
dictionnaire
```

---

### Exercice 6

Vérifie si :

```text
HOME
```

existe dans les variables d'environnement.

---

### Exercice 7

Réponds avec tes propres mots :

1. Qu'est-ce qu'une variable d'environnement ?
2. À quoi sert `os.getenv()` ?
3. Différence entre `getenv()` et `os.environ[]` ?
4. Pourquoi utiliser une valeur par défaut ?
5. Pourquoi stocker une clé API dans une variable d'environnement plutôt que dans le code ?