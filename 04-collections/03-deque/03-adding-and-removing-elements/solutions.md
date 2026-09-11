
# Exercices

## Exercice 1

Importe `deque`.

```python
from collections import deque
```

---

## Exercice 2

Complète :

| Méthode        | Rôle |
| -------------- | ---- |
| `append()`     | ajout à la fin    |
| `appendleft()` | ajout au début    |
| `pop()`        | suppression à la fin    |
| `popleft()`    | suppression au début    |

---

## Exercice 3

Complète :

```text
append()

↓

Ajout à droite
```

---

et

```text
appendleft()

↓

Ajout à gauche
```

---

## Exercice 4

Complète :

```text
pop()

↓

Suppression à droite
```

---

et

```text
popleft()

↓

Suppression à gauche
```

---

## Exercice 5

Associe :

| Action           | Méthode |
| ---------------- | ------- |
| Ajouter à droite | `append`     |
| Ajouter à gauche | `appendleft`     |
| Retirer à droite | `pop`     |
| Retirer à gauche | `popleft`     |

---

## Exercice 6

Complète :

```text
FIFO

↓

First In

↓

First Out
```

---

et

```text
LIFO

↓

Last In

↓

First Out
```

---

## Exercice 7

Associe :

| Situation               | Comportement |
| ----------------------- | ------------ |
| File d'attente          | `FIFO`       |
| Historique de tâches    | `LIFO`       |
| Impression de documents | `FIFO`       |
| Pile Undo               | `LIFO`       |

---

## Exercice 8

Parmi les méthodes suivantes, lesquelles modifient un deque ?

- `append()` : `oui`
- `appendleft()` : `oui`
- `pop()` : `oui`
- `popleft()` : `oui`

---

## Exercice 9

Réponds avec tes propres mots :

1. Quelle différence existe entre `append()` et `appendleft()` ?
    - `append()` ajoute un élément à la fin alors que `appendleft()` ajoute un élément au début.
2. Quelle différence existe entre `pop()` et `popleft()` ?
    - `pop()` supprime un élément à la fin alors que `popleft()` supprime un élément au début.
3. Qu'est-ce qu'un comportement FIFO ?
    - premier à entré - prémier à sortir
4. Qu'est-ce qu'un comportement LIFO ?
    - dernier à entré - premier à sortir
5. Dans quel projet personnel pourrais-tu utiliser ces méthodes ?
    - une file d'attente des demandes à valider