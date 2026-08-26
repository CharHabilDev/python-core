# Exercises

## Exercice 1

Crée la structure suivante :
```txt
project/
├── README.md
├── main.py
└── data/
    └── users.csv
```
---

## Exercice 2

Affiche le contenu de :

project/

avec `rglob()`.

---

## Exercice 3

Crée une archive ZIP :

project_backup.zip

à partir de :

project/

---

## Exercice 4

Vérifie que :

project_backup.zip

existe.

---

## Exercice 5

Crée un dossier :

sandbox/restored_project/

Puis extrait l'archive ZIP dans ce dossier.

---

## Exercice 6

Affiche le contenu de :

restored_project/

pour vérifier l'extraction.

---

## Exercice 7

Supprime :

project/

puis vérifie que les données sont toujours récupérables grâce à l'archive.

(Indice conceptuel : l'archive devient alors la seule copie restante.)

---

## Exercice 8

Réponds avec tes propres mots :

1. À quoi sert `shutil.make_archive()` ?
2. À quoi sert `shutil.unpack_archive()` ?
3. Pourquoi les archives sont-elles utiles ?
4. Quelle différence existe entre copier un dossier et créer une archive ?
5. Dans quel cas utiliserais-tu les archives dans un projet réel ?