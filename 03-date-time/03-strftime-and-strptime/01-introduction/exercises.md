# Exercices

### Exercice 1

```python
from datetime import datetime

print(datetime.strftime)
```

---

### Exercice 2

```python
from datetime import datetime

print(datetime.strptime)
```

---

### Exercice 3

```python
from datetime import datetime

help(datetime.strftime)
```

Puis :

```python
help(datetime.strptime)
```

---

### Exercice 4

Complète :

| Fonction     | Conversion |
| ------------ | ---------- |
| `strftime()` |            |
| `strptime()` |            |

---

### Exercice 5

Associe :

| Situation                            | Outil |
| ------------------------------------ | ----- |
| Afficher une date à un utilisateur   |       |
| Lire une date saisie au clavier      |       |
| Générer un rapport lisible           |       |
| Convertir une date texte en datetime |       |

---

### Exercice 6

Complète :

```text
datetime

↓

strftime()

↓

...
```

et

```text
texte

↓

strptime()

↓

...
```

---

### Exercice 7

Parmi les situations suivantes, quel outil utiliserais-tu principalement ?

- Affichage d'une date dans une interface
- Lecture d'une date depuis un formulaire
- Génération d'un reçu
- Import d'un fichier CSV contenant des dates
- Affichage d'un historique

---

### Exercice 8

Réponds avec tes propres mots :

1. Quel est le rôle de `strftime()` ?
2. Quel est le rôle de `strptime()` ?
3. Pourquoi les applications manipulent-elles souvent des dates sous forme de texte ?
4. Quelle différence existe entre un objet `datetime` et une chaîne de caractères ?
5. Cite un exemple réel où tu utiliserais les deux fonctions ensemble.