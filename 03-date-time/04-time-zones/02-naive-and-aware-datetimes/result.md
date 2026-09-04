## Exercices

### Exercice 1

Complète :

| Type           | Fuseau horaire ? |
| -------------- | ---------------- |
| Naive Datetime |  `non`           |
| Aware Datetime |  `oui`           |

---

### Exercice 2

Associe :

| Situation                             | Type |
| ------------------------------------- | ---- |
| Date sans fuseau                      |`Naive Datetime`     |
| Date avec UTC+1                       |`Aware Datetime`     |
| Date avec UTC                         |`Aware Datetime`      |
| Date sans information de localisation |`Naive Datetime`      |

---

### Exercice 3

Réponds :

Pourquoi cette date est-elle ambiguë ?

```text
2026-01-01 15:00
```
#### Réponse:
Parce qu'elle contient une date et une heure mais aucun fuseau horaire.
On ne sait donc pas à quel endroit du monde correspond ce 15:00.

---

### Exercice 4

Complète :

| Caractéristique            | Naive | Aware |
| -------------------------- | :---: | :---: |
| Contient une heure         | `Oui` | `Oui` |
| Contient une date          | `Oui` | `Oui` |
| Contient un fuseau horaire | `Non` | `Oui` |

---

### Exercice 5

Associe :

| Besoin                    | Type recommandé |
| ------------------------- | --------------- |
| Application locale simple | `Naive`                |
| Réseau social mondial     | `Aware`                |
| Réservation de vols       |  `Aware`               |
| Agenda international      | `Aware`                |

---

### Exercice 6

Complète :

```text
Naive Datetime

↓

pas de fuseau horaire

↓

Impossible de connaître le fuseau
```

et

```text
Aware Datetime

↓

fuseau horaire inclus

↓

Fuseau connu
```

---

### Exercice 7

Parmi les situations suivantes, lesquelles devraient utiliser des aware datetimes ?

- Réservation de vol : `oui`
- Réunion Zoom internationale : `oui`
- Horodatage mondial : `oui`
- Calculatrice simple : `non`
- Réseau social : `oui`

---

### Exercice 8

Réponds avec tes propres mots :

1. Qu'est-ce qu'un naive datetime ?
    - C'est un objet datetime qui ne contient aucune information sur son fuseau horaire
2. Qu'est-ce qu'un aware datetime ?
    - C'est un objet datetime qui contient une information de fuseau horaire
3. Pourquoi les aware datetimes sont-ils importants ?
    - parcequ'il permet d'identifier un instant précis
4. Quel risque existe lorsqu'on utilise uniquement des naive datetimes ?
    - risque de confusion entre plusieurs fuseaux horaires 
    - affichage d'heures incorrectes 
    - rendez-vous, réservations ou notifications au mauvais moment 
5. Dans quel type de projet personnel pourrais-tu rencontrer ce problème ?
    - Gestionnaire de tâches