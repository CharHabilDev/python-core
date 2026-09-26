# Exercices

## Exercice 1

Associe :

| Élément         | Description                                |
| --------------- | ------------------------------------------ |
| `itertools`     | module pour travailler avec des itérateurs |
| Iterable        | collection parcourable                     |
| Iterator        | produit des valeurs une par une            |
| Lazy Evaluation | création des valeurs à la demande          |

---

## Exercice 2

Complète :

```text
itertools
↓
travaille avec des
↓
itérateurs
```

---

## Exercice 3

Complète :

```text
Iterable
↓
collection de
↓
collection d'éléments
```

---

## Exercice 4

Complète :

```text
Iterator
↓
produit les valeurs
↓
une par une
```

---

## Exercice 5

Associe :

| Objet                | Type                |
| -------------------- | ------------------- |
| Liste                | Iterable            |
| Tuple                | Iterable            |
| Chaîne de caractères | Iterable            |
| Iterator             | Produit des valeurs |

---

## Exercice 6

Complète :

```text
Lazy Evaluation
↓
valeurs créées
↓
quand elles sont
↓
demandées
```

---

## Exercice 7

Vrai ou Faux ?

- `itertools` fait partie de la bibliothèque standard Python : `vrai`
- Un iterator stocke toujours toutes les valeurs en mémoire : `faux`
- Les outils de `itertools` retournent souvent des iterators : `vrai`
- La lazy evaluation permet de réduire l'utilisation mémoire : `vrai`

---

## Exercice 8

Associe :

| Catégorie               | Exemples                                        |
| ----------------------- | ----------------------------------------------- |
| Infinite Iterators      | `count()`, `cycle()`, `repeat()`                |
| Iterator Building Tools | `chain()`, `islice()`, `groupby()`              |
| Combinatoric Iterators  | `product()`, `permutations()`, `combinations()` |

---

## Exercice 9

Complète :

```text
itertools
↓
iterators
↓
lazy evaluation
↓
moins de mémoire
↓
traitement efficace
```

---

## Exercice 10

Réponds avec tes propres mots :

1. Pourquoi le module `itertools` existe-t-il ?
    - pour éviter d'utiliser plusieurs boucles et de créer des listes intermédiaire pour le 
    traitement de certaines données.

2. Quelle différence existe entre un iterable et un iterator ?
    - un iterable peut être parcouru, alors qu'un iterator fournit les valeurs une par une à la demande.

3. Qu'est-ce que la lazy evaluation ?
    - la lazy evaluation consiste à produire les valeurs uniquement lorsqu'elles sont demandées.

4. Quels sont les principaux avantages de la lazy evaluation ?
    - moins de mémoire utilise
    - meilleurs performances

5. Cite les trois grandes catégories d'outils présentes dans `itertools`.
    - `Infinite Iterators`
    - `Iterator Building Tools`
    - `Combinatoric Iterators`

6. Quel lien peux-tu faire entre un iterator et un générateur utilisant `yield` ?
    - un générateur utilisant yield est un type d'iterator.
    Il produit les valeurs une par une lorsqu'elles sont demandées avec next().