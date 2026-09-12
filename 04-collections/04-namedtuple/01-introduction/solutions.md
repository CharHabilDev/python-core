# Exercices

## Exercice 1

Importe `namedtuple`.

```python
from collections import namedtuple
```

---

## Exercice 2

Complète :

| Élément       | Rôle |
| ------------- | ---- |
| `collections` | module contenant plusieurs structures de données |
| `namedtuple`  | tuple nommé    |

---

## Exercice 3

Complète :

```text
namedtuple

↓

tuple nommé
```

---

## Exercice 4

Associe :

| Situation                   | Outil        |
| --------------------------- | ------------ |
| Représenter une personne    | `namedtuple` |
| Représenter un étudiant     | `namedtuple` |
| Représenter un produit      | `namedtuple` |
| Représenter des coordonnées | `namedtuple` |

---

## Exercice 5

Complète :

```text
tuple

↓

("Alice", 25, "Belgium")

↓

tuple[index]
```

---

et

```text
namedtuple

↓

Person

↓

name
age
country

↓

person.name
person.age
person.country
```

---

## Exercice 6

Associe :

| Caractéristique | tuple | namedtuple |
| --------------- | :---: | :--------: |
| Ordonné         | `oui` |    `oui`   |
| Immuable        | `oui` |    `oui`   |
| Accès par index | `oui` |    `oui`   |
| Accès par nom   | `non` |    `oui`   |

---

## Exercice 7

Parmi les situations suivantes, lesquelles pourraient utiliser `namedtuple` ?

* Gestion d'étudiants : `oui`
* Catalogue de produits : `oui`
* Coordonnées GPS : `oui`
* Calculatrice : `non`
* Données d'un lapin : `oui`

---

## Exercice 8

Complète :

```text
tuple

↓

valeurs

↓

indices
```

---

et

```text
namedtuple

↓

valeurs

↓

nom
```

---

## Exercice 9

Réponds avec tes propres mots :

1. Quel est le rôle de `namedtuple` ?
    - `namedtuple` permet de créer un tuple dont les valeurs sont accessibles par des noms de champs.
2. Pourquoi est-il plus lisible qu'un tuple classique ?
    - parceque qu'on sait ce que que représente la valeur obtenu
3. Quel problème résout-il ?
    - lisiblité
4. Cite deux exemples où `namedtuple` pourrait être utilisé.
    - une personne
    - un produit
5. Dans quel projet personnel pourrais-tu utiliser `namedtuple` ?
    - Rabbit Manager