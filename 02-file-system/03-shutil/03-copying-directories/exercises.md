# Exercises

## Exercice 1

Crée la structure suivante :

```text
sandbox/
└── project/
    ├── README.md
    ├── notes.txt
    └── data/
        └── users.csv
```

---

## Exercice 2

Affiche le contenu du dossier :

```text
project/
```

en utilisant `rglob()`.

---

## Exercice 3

Copie :

```text
project/
```

vers :

```text
project_backup/
```
---

## Exercice 4

Vérifie que :

```text
project_backup/
```

existe.

---

## Exercice 5

Affiche le contenu de :

```text
project_backup/
```

et vérifie que tous les fichiers ont été copiés.

---

## Exercice 6

Essaie d'exécuter à nouveau :

```python
shutil.copytree(
    source,
    destination
)
```

sans supprimer :

```text
project_backup/
```

Observe l'erreur obtenue.

---

## Exercice 7

Recommence avec :

```python
dirs_exist_ok=True
```

Observe le résultat.

---

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `copytree()` ?
2. Quelle différence existe entre `copy()` et `copytree()` ?
3. Pourquoi la destination ne doit-elle pas exister par défaut ?
4. À quoi sert `dirs_exist_ok=True` ?
5. Dans quel cas utiliserais-tu `copytree()` dans un projet réel ?