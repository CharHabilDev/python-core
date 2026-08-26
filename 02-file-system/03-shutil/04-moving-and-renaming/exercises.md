# Exercises

## Exercice 1

Crée la structure suivante :

```txt
sandbox/
└── files/
    ├── notes.txt
    └── report.txt
```
---

## Exercice 2

Affiche le contenu de :

```txt
files/
```

---

## Exercice 3

Crée un dossier :

archives/

puis déplace :

notes.txt

vers :

archives/

---

## Exercice 4

Vérifie que :

- notes.txt n'existe plus dans files/
- notes.txt existe dans archives/

---

## Exercice 5

Renomme :

report.txt

en :

annual_report.txt

avec `shutil.move()`.

---

## Exercice 6

Affiche le contenu final de :

files/

et de :

archives/

---

## Exercice 7

Crée :

sandbox/project/

avec quelques fichiers.

Puis déplace tout le dossier vers :

sandbox/project_backup/

---

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `shutil.move()` ?
2. Quelle différence existe entre `copy()` et `move()` ?
3. Pourquoi vérifier que la source n'existe plus après un déplacement ?
4. Comment renommer un fichier avec `move()` ?
5. Dans quel cas utiliserais-tu `move()` dans un projet réel ?