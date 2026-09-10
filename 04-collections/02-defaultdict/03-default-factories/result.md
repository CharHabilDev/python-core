# Exercices

## Exercice 1

Complète :

| Factory | Valeur par défaut |
| ------- | ----------------- |
| `int`   | 0                 |
| `list`  | []                 |
| `set`   | set()                 |

---

## Exercice 2

Associe :

| Besoin                   | Factory |
| ------------------------ | ------- |
| Compter des votes        | `int`       |
| Regrouper des étudiants  | `list`       |
| Stocker des tags uniques | `set`       |
| Compter des mots         | `int`       |

---

## Exercice 3

Complète :

```text
clé absente
↓
defaultdict(set)
↓
set()
```

---

et

```text
clé absente
↓
defaultdict(list)
↓
[]
```

---

## Exercice 4

Réponds avec tes propres mots :

1. Quelle différence existe entre `list` et `set` comme factory ?
    - `list` stocke toutes les valeurs sans se soucier des doublons contrairement à `set`
2. Quand choisir `int` ?
    - si on veut compter
3. Pourquoi `set` est-il utile ?
    - parce qu'il permet d'éviter les doublons sans faire d'opération supplémentaire
4. Cite deux situations où `defaultdict(set)` est pertinent.
    - tags d'articles
    - catégories de produits
5. Dans quel projet personnel pourrais-tu utiliser `defaultdict(set)` ?
    ```text
    Rabbit Manager
    ↓
    race → identifiants uniques des lapins 
    ```