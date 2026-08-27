# Exercises

## Exercice 1

Importe :

```python
import tempfile
```

Crée un objet :

```python
tempfile.TemporaryFile()
```

Affiche son type.

---

## Exercice 2

Crée un fichier temporaire.

Affiche l'objet retourné.

Observe le résultat.

---

## Exercice 3

Écris le texte :

```text
Bonjour tempfile
```

dans le fichier temporaire.

---

## Exercice 4

Replace le curseur au début du fichier.

Lis le contenu.

Affiche le résultat.

---

## Exercice 5

Ferme le fichier temporaire.

Vérifie que l'opération réussit.

---

## Exercice 6

Crée un :

```python
tempfile.NamedTemporaryFile()
```

Affiche :

```python
temp.name
```

Observe le chemin généré.

---

## Exercice 7

Complète :

| Outil                | Particularité |
| -------------------- | ------------- |
| TemporaryFile()      | ?             |
| NamedTemporaryFile() | ?             |
| seek(0)              | ?             |
| name                 | ?             |

---

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `TemporaryFile()` ?
2. À quoi sert `NamedTemporaryFile()` ?
3. Pourquoi utiliser `seek(0)` ?
4. Dans quel cas aurais-tu besoin d'un nom de fichier visible ?
5. Quelle différence principale existe entre les deux objets ?