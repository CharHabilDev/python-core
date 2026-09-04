## Exercices

### Exercice 1

Complète :

| Type           | Fuseau horaire ? |
| -------------- | ---------------- |
| Naive Datetime |                  |
| Aware Datetime |                  |

---

### Exercice 2

Associe :

| Situation                             | Type |
| ------------------------------------- | ---- |
| Date sans fuseau                      |      |
| Date avec UTC+1                       |      |
| Date avec UTC                         |      |
| Date sans information de localisation |      |

---

### Exercice 3

Réponds :

Pourquoi cette date est-elle ambiguë ?

```text
2026-01-01 15:00
```

---

### Exercice 4

Complète :

| Caractéristique            | Naive | Aware |
| -------------------------- | :---: | :---: |
| Contient une heure         |       |       |
| Contient une date          |       |       |
| Contient un fuseau horaire |       |       |

---

### Exercice 5

Associe :

| Besoin                    | Type recommandé |
| ------------------------- | --------------- |
| Application locale simple |                 |
| Réseau social mondial     |                 |
| Réservation de vols       |                 |
| Agenda international      |                 |

---

### Exercice 6

Complète :

```text
Naive Datetime

↓

?

↓

Impossible de connaître le fuseau
```

et

```text
Aware Datetime

↓

?

↓

Fuseau connu
```

---

### Exercice 7

Parmi les situations suivantes, lesquelles devraient utiliser des aware datetimes ?

- Réservation de vol
- Réunion Zoom internationale
- Horodatage mondial
- Calculatrice simple
- Réseau social

---

### Exercice 8

Réponds avec tes propres mots :

1. Qu'est-ce qu'un naive datetime ?
2. Qu'est-ce qu'un aware datetime ?
3. Pourquoi les aware datetimes sont-ils importants ?
4. Quel risque existe lorsqu'on utilise uniquement des naive datetimes ?
5. Dans quel type de projet personnel pourrais-tu rencontrer ce problème ?