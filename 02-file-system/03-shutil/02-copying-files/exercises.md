# Exercises

## Exercice 1

Crée un dossier de test.

À l'intérieur, crée :

```text
source.txt
```

---

## Exercice 2

Écris quelques lignes dans :

```text
source.txt
```

---

## Exercice 3

Copie :

```text
source.txt
```

vers :

```text
copy.txt
```

avec `shutil.copy()`.

---

## Exercice 4

Vérifie que :

* les deux fichiers existent ;
* leur contenu est identique.

---

## Exercice 5

Supprime :

```text
copy.txt
```

puis recrée-le avec :

```python
shutil.copy2()
```

---

## Exercice 6

Copie :

```text
source.txt
```

dans un dossier nommé :

```text
backup/
```

---

## Exercice 7

Réponds avec tes propres mots :

1. À quoi sert `shutil.copy()` ?
2. Quelle différence existe entre `copy()` et `copy2()` ?
3. Pourquoi utiliser `Path` avec `shutil` ?
4. Que se passe-t-il si le fichier de destination existe déjà ?
5. Dans quel cas utiliserais-tu `copy2()` plutôt que `copy()` ?

```

Ce chapitre est le premier où `shutil` modifie réellement des fichiers. Rien de dangereux ici : au pire tu obtiens plusieurs copies du même document. La phase suivante commencera à déplacer les fichiers. Ensuite viendra `rmtree()`, qui est le genre de fonction qui rappelle pourquoi les sauvegardes ont été inventées.
```
