# Exercises

## Exercice 1

Importe :

```python
import tempfile
```

Crée un :

```python
tempfile.TemporaryDirectory()
```

Affiche son type.

---

## Exercice 2

Crée un dossier temporaire.

Affiche :

```python
temp_dir.name
```

Observe le chemin généré.

---

## Exercice 3

Transforme ce chemin en objet :

```python
Path(...)
```

Affiche l'objet obtenu.

---

## Exercice 4

Dans ce dossier temporaire :

* crée un fichier `notes.txt`
* vérifie qu'il existe

---

## Exercice 5

Crée un sous-dossier :

```text
data/
```

dans le dossier temporaire.

Vérifie son existence.

---

## Exercice 6

Affiche tout le contenu du dossier temporaire avec :

```python
iterdir()
```

---

## Exercice 7

Complète :

| Outil                | Rôle |
| -------------------- | ---- |
| TemporaryDirectory() | ?    |
| name                 | ?    |
| Path(...)            | ?    |
| iterdir()            | ?    |

---

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `TemporaryDirectory()` ?
2. Pourquoi utiliser un dossier temporaire plutôt qu'un fichier temporaire ?
3. Pourquoi utiliser `Path()` avec un dossier temporaire ?
4. Quel avantage apporte la suppression automatique ?
5. Dans quel cas utiliserais-tu un dossier temporaire dans un projet réel ?

```

Cette fois, tu vas manipuler un espace de travail temporaire complet. C'est très proche de ce que font beaucoup d'outils réels : ils créent un dossier temporaire, travaillent dedans, puis le détruisent une fois le travail terminé. Une attitude étonnamment mature pour un programme informatique.
```
