# Exercices

## Exercice 1

Complète :

| Élément | Rôle |
|----------|----------|
| `type_name` | nom du nouveau type |
| `field_names` | nom des champs |

---

## Exercice 2

Complète :

```text
namedtuple()

↓

new type

↓

instances
```

---

## Exercice 3

Complète :

```python
Person = namedtuple(
    "Person",
    ['name', 'age']
)
```

---

## Exercice 4

Associe :

| Élément     | Exemple   |
| ----------- | --------- |
| Nom du type | `Person`  |
| Champ       | `name`    |
| Champ       | `age`     |
| Champ       | `country` |

---

## Exercice 5

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

## Exercice 6

Associe :

| Situation | Type possible |
| --------- | ------------- |
| Personne  | `Person`      |
| Produit   | `Product`     |
| Lapin     | `Rabbit`      |
| Étudiant  | `Student`     |

---

## Exercice 7

Parmi les noms suivants, lesquels sont de bons noms de champs ?

* `name` : `oui`
* `age` : `oui`
* `country` : `oui`
* `x` : `non`
* `value` : `non`

---

## Exercice 8

Complète :

```text
namedtuple

↓

structure

↓

instances

↓

objets
```

---

## Exercice 9

Réponds avec tes propres mots :

1. Comment crée-t-on un namedtuple ?
    - on définit un nom de type et une liste de champs.
2. Quel est le rôle du nom du type ?
    - permet d'identifier l'objet crée
3. Quel est le rôle des champs ?
    - définir les champs des données afin de pouvoir y accéder sans utiliser d'index.
4. Cite deux exemples de namedtuple.
    - Rabbit
    - Student
5. Dans quel projet personnel pourrais-tu créer un namedtuple ?
    - Rabbit Manager