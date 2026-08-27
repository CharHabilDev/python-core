# Exercises

## Exercice 1

Complète le tableau :

| Critère | Fichier manuel | tempfile |
|----------|----------|----------|
| Nom unique | ? | ? |
| Nettoyage automatique | ? | ? |
| Gestion des erreurs | ? | ? |

---

## Exercice 2

Pour chaque situation, indique :

```text
Manuel
tempfile
```

### Situation A

Fichier intermédiaire de conversion PDF.

### Situation B

Configuration de l'application.

### Situation C

Cache temporaire.

### Situation D

Base de données principale.

### Situation E

Extraction temporaire d'une archive.

---

## Exercice 3

Explique pourquoi cette approche peut être risquée :

```python
Path("temp.txt")
```

---

## Exercice 4

Cite deux avantages de `tempfile`.

---

## Exercice 5

Cite deux situations où un fichier manuel est préférable.

---

## Exercice 6

Complète :

```text
Fichier temporaire
↓
...

Fichier permanent
↓
...

Nom unique
↓
...
```

---

## Exercice 7

Tu développes une application qui :

1. génère un rapport ;
2. crée plusieurs fichiers intermédiaires ;
3. produit un PDF final.

Quels fichiers devraient être temporaires et lesquels devraient être permanents ?

---

## Exercice 8

Réponds avec tes propres mots :

1. Pourquoi `tempfile` est-il plus sûr ?
2. Quel problème résout-il principalement ?
3. Quand préférerais-tu créer un fichier manuellement ?
4. Pourquoi les fichiers oubliés peuvent-ils devenir un problème ?
5. Résume la différence entre `tempfile` et un fichier manuel en une phrase.

```

Ce dernier chapitre sert surtout de synthèse du module. Après lui, tu auras couvert l'ensemble des concepts importants de `tempfile`, ce qui est assez rapide comparé à `os` ou `pathlib`. Les concepteurs de ce module ont eu la décence de ne pas transformer une idée simple en une jungle de sous-modules. Une rare victoire de la simplicité dans le monde logiciel.
```
