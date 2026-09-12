# Exercices

## Exercice 1

Associe :

| Élément | Rôle |
|----------|----------|
| `_fields` | obtenir les champs d'un `namedtuple` |
| `_asdict()` | convertir un `namedtuple` en `dict` |
| `_replace()` | copier et modifier des valeurs d'un `namedtuple` |
| `_make()` | créer un `nametuple` à partir d'un itérable |

---

## Exercice 2

Complète :

```text
namedtuple

↓

_fields

↓

champs
```

---

## Exercice 3

Complète :

```text
namedtuple

↓

_asdict()

↓

dict
```

---

## Exercice 4

Complète :

```text
iterable

↓

_make()

↓

namedtuple
```

---

## Exercice 5

Complète :

```text
namedtuple

↓

_replace()

↓

new instance
```

---

## Exercice 6

Associe :

| Situation                   | Outil        |
| --------------------------- | ------------ |
| Obtenir les noms des champs | `_fields`    |
| Convertir en dictionnaire   | `_asdict()`  |
| Créer depuis une liste      | `_make()`    |
| Modifier une valeur         | `_replace()` |

---

## Exercice 7

Parmi les affirmations suivantes, lesquelles sont vraies ?

* `_fields` retourne les champs : `oui`
* `_asdict()` retourne un dictionnaire : `oui`
* `_replace()` modifie l'objet original : `non`
* `_make()` peut utiliser une liste : `oui`

---

## Exercice 8

Complète :

```text
namedtuple

↓

immutable

↓

_replace()

↓

nouvelle instance
```

---

## Exercice 9

Réponds avec tes propres mots :

1. Quel est le rôle de `_fields` ?
    - obtenir les noms des champs du namedtuple
2. Quel est le rôle de `_asdict()` ?
    - convertir un namedtuple en dictionnaire
3. Pourquoi utilise-t-on `_replace()` ?
    - parce que, comme un tuple, un namedtuple est immuable
4. Quel est le rôle de `_make()` ?
    - créer un namedtuple à partir d'un itérable
5. Dans quel projet personnel pourrais-tu utiliser une de ces fonctionnalités ?
    - Rabbit Manager