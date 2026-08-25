# Exercices

## Exercice 1

Crée un chemin vers :

```text
documents/notes.txt
```

avec :

- `os`
- `pathlib`

Affiche les deux résultats.

---

### Exercice 2

Vérifie l'existence d'un fichier :

- une fois avec `os`
- une fois avec `pathlib`

Compare les deux approches.

---

### Exercice 3

Vérifie qu'un élément est un fichier :

- une fois avec `os`
- une fois avec `pathlib`

Compare la lisibilité du code.

---

### Exercice 4

Vérifie qu'un élément est un dossier :

- une fois avec `os`
- une fois avec `pathlib`

Compare les deux solutions.

---

### Exercice 5

Réécris ce code utilisant `os` avec `pathlib` :

```python
import os

path = os.path.join(
    "images",
    "photo.jpg"
)

print(os.path.exists(path))
```

---

### Exercice 6

Réécris ce code utilisant `os` avec `pathlib` puis explique laquelle des deux versions te semble la plus lisible :

```python
import os

path = os.path.join(
    "documents",
    "cours",
    "python",
    "notes.txt"
)

print(path)
```

---

Ou encore :

### Exercice 6

Liste les avantages et inconvénients de :

```text
os.path
```

et :

```text
pathlib
```

après avoir testé les deux pendant ce chapitre.

---

## Exercice 7

Réponds avec tes propres mots :

1. Pourquoi `pathlib` a-t-il été introduit ?
2. Quelle différence principale vois-tu entre `os.path` et `Path` ?
3. Dans quel cas utiliserais-tu encore `os` ?
4. Pourquoi beaucoup de projets modernes préfèrent-ils `pathlib` ?
5. Quel module utiliserais-tu pour gérer des variables d'environnement ?