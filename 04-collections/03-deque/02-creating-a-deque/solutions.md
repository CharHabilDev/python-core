# Exercices

## Exercice 1

Importe `deque`.

```python
from collections import deque
```

---

## Exercice 2

Crée un deque à partir :

- d'une liste
    ```py
    deque(['pomme', 'orange'])
    ```
- d'un tuple
    ```py
    deque(('pomme', 'orange'))
    ```
- d'une chaîne de caractères
    ```py
    deque("pomme")
    ```

---

## Exercice 3

Complète :

```text
Liste

↓

deque()

↓

deque([...])
```

---

## Exercice 4

Complète :

```text
Tuple

↓

deque()

↓

deque([...])
```

---

## Exercice 5

Complète :

```text
Chaîne

↓

deque()

↓

chaque caractère devient un élément
```

---

## Exercice 6

Associe :

| Source | Compatible avec deque ? |
| ------ | ----------------------- |
| Liste  | `oui`                   |
| Tuple  | `oui`                   |
| Chaîne | `oui`                   |
| Range  | `oui`                   |
| Entier | `non`                   |

---

## Exercice 7

Complète :

```text
Iterable

↓

deque()

↓

Deque Object
```

---

## Exercice 8

Parmi les éléments suivants, lesquels peuvent être utilisés pour créer un deque ?

- Liste : `oui`
- Tuple : `oui`
- Chaîne : `oui`
- Range : `oui`
- Entier : `non`

---

## Exercice 9

Réponds avec tes propres mots :

1. Comment crée-t-on un deque ?
    - il faut passer en argument un obejet itérable à `deque` (`deque(arg)`).
2. Quels types de données peuvent être utilisés pour créer un deque ?
    - une liste, un tuple, une chaine ou un range
3. Pourquoi un entier ne peut-il pas être utilisé directement ?
    - parcequ'il n'est pas itérable
4. Cite deux exemples de création d'un deque.
    - deque(["apple", "banana"])
    - deque("hello")
5. Dans quel projet personnel pourrais-tu créer un deque ?
    - Trend Tracker : conserver les dernières tendances observées.