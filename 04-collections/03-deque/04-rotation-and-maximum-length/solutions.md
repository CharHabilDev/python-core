````md
# Exercices

## Exercice 1

Complète :

| Élément | Rôle |
|----------|----------|
| `rotate()` | déplacer des éléments d'une extrémité à l'autre |
| `maxlen` | définir la taille maximale d'un deque |

---

## Exercice 2

Complète :

```text
rotate(1)

↓

[1] [2] [3] [4]

↓

[4] [1] [2] [3]
````

---

## Exercice 3

Complète :

```text
rotate(-1)

↓

[1] [2] [3] [4]

↓

[2] [3] [4] [1]
```

---

## Exercice 4

Associe :

| Action                  | Résultat                        |
| ----------------------- | ------------------------------- |
| `rotate(1)`             | dernier élément devient premier |
| `rotate(-1)`            | premier élément devient dernier |
| `maxlen=3`              | taille limitée                  |
| dépassement de `maxlen` | suppression automatique         |

---

## Exercice 5

Complète :

```text
maxlen = 3

[A] [B] [C]

append(D)

↓

[B] [C] [D]
```

---

## Exercice 6

Parmi les situations suivantes, lesquelles pourraient utiliser `rotate()` ?

- Jeu à tour de rôle : `oui`
- Ordonnancement circulaire : `oui`
- Historique navigateur : `non`
- Rotation d'équipes : `oui`
- Calculatrice : `non`

---

## Exercice 7

Parmi les situations suivantes, lesquelles pourraient utiliser `maxlen` ?

- Historique récent : `oui`
- Dernières notifications : `oui`
- Buffer de logs : `oui`
- Calculatrice : `non`
- Dernières recherches : `oui`

---

## Exercice 8

Complète :

```text
deque(maxlen=5)

↓

taille limitée à 5

↓

6e élément ajouté

↓

premier élément supprimé
```

---

## Exercice 9

Réponds avec tes propres mots :

1. Quel est le rôle de `rotate()` ?
    - déplacer les éléments d'un deque d'une extrémité vers l'autre
2. Quelle différence existe entre `rotate(1)` et `rotate(-1)` ?
    - `rotate(1)` déplace le dernier élément à la première place alors que `rotate(-1)` déplace le prémier élément à la dernière place
3. Quel est le rôle de `maxlen` ?
    - - limiter le nombre de valeurs que peut contenir un deque
4. Que se passe-t-il lorsqu'un deque atteint sa taille maximale ?
    - l'élément le plus ancien est automatiquement supprimé.
5. Dans quel projet personnel pourrais-tu utiliser `rotate()` ou `maxlen` ?
    - événements qui se répètent (rotate(-1))
    - recherches récentes (maxlen)