# Exercises

## Exercice 1

Crée la structure suivante :
```txt
sandbox/
└── project/
    ├── README.md
    ├── main.py
    └── data/
        └── users.csv
```

---

## Exercice 2

Affiche tout le contenu de :

project/

avec `rglob()`.

---

## Exercice 3

Vérifie que :

project/

existe.

---

## Exercice 4

Essaie de supprimer :

project/

avec :

`Path.rmdir()`

Observe l'erreur obtenue.

---

## Exercice 5

Supprime :

project/

avec :

`shutil.rmtree()`

---

## Exercice 6

Vérifie que :

project/

n'existe plus.

---

## Exercice 7

Crée :

sandbox/temp/

avec quelques fichiers.

Ajoute une vérification :

- le dossier existe ;
- c'est bien un dossier.

Puis supprime-le avec :

```python
shutil.rmtree(...)
```

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `shutil.rmtree()` ?
2. Quelle différence existe entre `rmdir()` et `rmtree()` ?
3. Pourquoi `rmdir()` échoue-t-il sur un dossier non vide ?
4. Pourquoi faut-il être prudent avec `rmtree()` ?
5. Dans quel cas utiliserais-tu `rmtree()` dans un projet réel ?