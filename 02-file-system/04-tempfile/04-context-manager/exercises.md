# Exercises

## Exercice 1

Importe :

```python
import tempfile
```

Crée un :

```python
with tempfile.TemporaryFile() as temp:
```

Affiche son type.

---

## Exercice 2

Dans le bloc `with` :

- écris :

```text
Bonjour Context Manager
```

- lis le contenu
- affiche le résultat

---

## Exercice 3

Explique pourquoi il faut utiliser :

```python
seek(0)
```

avant la lecture.

---

## Exercice 4

Crée un :

```python
with tempfile.NamedTemporaryFile() as temp:
```

Affiche :

```python
temp.name
```

---

## Exercice 5

Crée un :

```python
with tempfile.TemporaryDirectory() as temp_dir:
```

Transforme le chemin en :

```python
Path(...)
```

et affiche-le.

---

## Exercice 6

Dans ce dossier temporaire :

- crée `notes.txt`
- crée `data/`
- affiche le contenu du dossier

---

## Exercice 7

Complète :

| Élément              | Rôle |
| -------------------- | ---- |
| with                 | ?    |
| as                   | ?    |
| TemporaryFile()      | ?    |
| TemporaryDirectory() | ?    |
| seek(0)              | ?    |

---

## Exercice 8

Réponds avec tes propres mots :

1. Quel est le rôle de `with` ?
2. Pourquoi est-il plus sûr que la gestion manuelle ?
3. Quel avantage apporte le nettoyage automatique ?
4. Pourquoi utilise-t-on souvent `with` avec `tempfile` ?
5. Dans quels autres modules Python as-tu déjà vu `with` ?