# Exercices

## Exercice 1

Affiche :

```python
os.getcwd()
```

---

## Exercice 2

Crée un dossier :

```text
test_directory
```

Puis :

- affiche le dossier courant ;
- entre dans ce dossier avec `os.chdir()` ;
- affiche à nouveau le dossier courant.

Observe la différence.

---

## Exercice 3

Depuis `test_directory` :

- crée un dossier `data` ;
- affiche le contenu du dossier courant avec `os.listdir()`.

---

## Exercice 4

Sauvegarde le dossier initial dans une variable.

Navigue vers `test_directory`.

Puis retourne au dossier initial.

Affiche les deux chemins.

---

## Exercice 5

Affiche :

```python
os.listdir()
```

avant et après un changement de dossier.

Observe la différence.

---

## Exercice 6

Nettoie les dossiers créés pendant les exercices.

---

## Exercice 7

Réponds avec tes propres mots :

1. À quoi sert `os.getcwd()` ?
2. À quoi sert `os.chdir()` ?
3. Pourquoi le dossier courant est-il important ?
4. Pourquoi certaines erreurs `FileNotFoundError` sont-elles liées au dossier courant ?
5. Pourquoi est-il souvent utile de sauvegarder le dossier initial avant de le modifier ?