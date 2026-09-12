# Exercices

## Exercice 1

Complète :

| Méthode | Exemple |
|----------|----------|
| Accès par nom | `student.name` |
| Accès par index | `student[0]` |

---

## Exercice 2

Complète :

```text
Person

↓

name
age
country

↓

person
```

---

## Exercice 3

Complète :

```python
person.name
```

pour accéder au nom.

---

## Exercice 4

Complète :

```python
person[0]
```

pour accéder au premier élément.

---

## Exercice 5

Associe :

| Expression       | Signification |
| ---------------- | ------------- |
| `person.name`    | nom           |
| `person.age`     | âge           |
| `person.country` | pays          |

---

## Exercice 6

Associe :

| Accès        | Lisibilité |
| ------------ | ---------- |
| `person[1]`  | faible     |
| `person.age` | élevée     |

---

## Exercice 7

Parmi les expressions suivantes, lesquelles utilisent un accès par nom ?

- `person.name` : `oui`
- `person[0]` : `non`
- `person.age` : `oui`
- `person[1]` : `non`

---

## Exercice 8

Complète :

```text
namedtuple

↓

champ

↓

accès par nom
```

---

## Exercice 9

Réponds avec tes propres mots :

1. Comment accéder à un champ d'un namedtuple ?
    - - avec la syntaxe instance.champ
2. Quelle différence existe entre `person.name` et `person[0]` ?
    - person.name indique directement ce que l'on obtient, contrairement à person[0].
3. Pourquoi l'accès par nom est-il plus lisible ?
    - parce qu'il permet de savoir ce qu'on obtient
4. Cite deux exemples d'accès à des champs.
    - rabbit.breed
    - rabbit.gender
5. Dans quel projet personnel pourrais-tu utiliser cette fonctionnalité ?
    - Rabbit Manager