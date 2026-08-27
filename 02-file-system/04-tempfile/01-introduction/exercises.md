# Exercises

## Exercice 1

Importe le module :

```python
import tempfile
```

Affiche son type avec :

```python
type(tempfile)
```

---

## Exercice 2

Affiche l'aide du module :

```python
help(tempfile)
```

Observe les principales fonctions disponibles.

---

## Exercice 3

Parmi les éléments suivants, indique lesquels pourraient être temporaires :

- fichier téléchargé avant traitement
- rapport final envoyé au client
- cache d'une application
- fichier intermédiaire de conversion PDF
- base de données de production

---

## Exercice 4

Complète le tableau :

| Situation                       | Temporaire ? |
| ------------------------------- | ------------ |
| Fichier de test                 | ?            |
| Rapport final                   | ?            |
| Cache                           | ?            |
| Archive intermédiaire           | ?            |
| Données utilisateur permanentes | ?            |

---

## Exercice 5

Associe chaque besoin à l'outil approprié :

| Besoin                                          | Outil |
| ----------------------------------------------- | ----- |
| Créer un fichier temporaire                     | ?     |
| Créer un dossier temporaire                     | ?     |
| Créer un fichier temporaire avec un nom visible | ?     |

---

## Exercice 6

Explique pourquoi cette approche est risquée :

```python
Path("temp.txt")
```

puis plus tard :

```python
unlink()
```

---

## Exercice 7

Complète :

```text
Créer
↓
...
↓
...
```

---

## Exercice 8

Réponds avec tes propres mots :

1. Quel est le rôle du module `tempfile` ?
2. Quel problème cherche-t-il à résoudre ?
3. Pourquoi les noms générés automatiquement sont-ils utiles ?
4. Dans quel cas utiliserais-tu un fichier temporaire ?
5. Dans quel cas ne faudrait-il pas utiliser un fichier temporaire ?

