# Exercices

## Exercice 1

Importe `deque`.

```python
from collections import deque
```

---

## Exercice 2

Complète :

| Élément       | Rôle |
| ------------- | ---- |
| `collections` | module contenant plusieurs structures de données spécialisées    |
| `deque`       |  ajout ou suppression aux deux extrémités    |

---

## Exercice 3

Complète :

```text
deque

↓

file à double extrémité
```

---

## Exercice 4

Associe :

| Situation              | Outil   |
| ---------------------- | ------- |
| File d'attente         | `deque` |
| Historique navigateur  | `deque` |
| Système Undo/Redo      | `deque` |
| Traitement de messages | `deque` |

---

## Exercice 5

Parmi les situations suivantes, lesquelles pourraient utiliser `deque` ?

- Historique navigateur : `oui`
- File d'impression : `oui`
- Calculatrice : `non`
- Gestion de tâches : `oui`
- Traitement de logs : `oui`

---

## Exercice 6

Complète :

```text
Ajout / Suppression

↓

Gauche et Droite

↓

deque
```

---

## Exercice 7

Réponds avec tes propres mots :

1. Quel est le rôle de `deque` ?
    - permettre l'ajout et la suppression efficaces d'éléments aux deux extrémités d'une séquence.
2. Pourquoi `deque` existe-t-il alors que les listes existent déjà ?
    - parce qu'il est optimisé pour les insertions et suppressions au début et à la fin d'une séquence.
3. Quel problème résout-il ?
    - il évite les ralentissements liés aux insertions et suppressions fréquentes au début d'une liste.
4. Cite deux situations où `deque` pourrait être utilisé.
    - file d'attente d'un service numérique
    - historique de navigation d'un navigateur
5. Dans quel projet personnel pourrais-tu utiliser `deque` ?
    - Tendance Tracker