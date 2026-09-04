# Exercices

### Exercice 1

Associe :

| Situation             | Outil principal |
| --------------------- | --------------- |
| Réservation           | `datetime`      |
| Abonnement            | `timedelta`     |
| Affichage utilisateur | `strftime()`    |
| Calcul de durée       | `timedelta`     |


---

### Exercice 2

Complète :

| Besoin                           | Solution |
| -------------------------------- | -------- |
| Lire une date utilisateur        |`strptime()`          |
| Afficher une date lisible        |`strftime()`          |
| Ajouter 30 jours                 |`timedelta`          |
| Calculer une différence de temps |`datetime - datetime`          |

---

### Exercice 3

Pour chaque situation, indique les outils utilisés :

- Réservation d'hôtel
    - `strptime()` pour convertir la date d'arrivée et de départ en datetime
    - `timedelta` pour calculer la durée du séjour
- Gestion d'abonnement
    - `datetime/date` pour enregister la date de début
    - `timedelta` pour calculer l'échéance
- Calendrier
    - `datetime` pour les rappels et événement
    - `strftime()` pour l'affichage des événements
- Livraison
    - `datetime` date estimée de livraison
    - `timedelta` délai restant
    - `strftime()` affichage utilisateur
- Système de rappel
    - `datetime` date du rappel
    - `timedelta` délai restant
    - `strftime()` affichage de la notification
---

### Exercice 4

Complète :

| Objet        | Rôle |
| ------------ | ---- |
| `datetime`   |représente un instant précis      |
| `timedelta`  |représente une durée      |
| `strftime()` |convertion `datetime` to `str`      |
| `strptime()` |convertion `str` to `datetime`      |

---

### Exercice 5

Associe :

| Action                        | Outil |
| ----------------------------- | ----- |
| Convertir un texte en date    |`strptime()`       |
| Convertir une date en texte   |`strftime()`       |
| Représenter une durée         |`timedelta`       |
| Représenter un instant précis |`datetime`       |

---

### Exercice 6

Complète :

```text id="5v5bte"
input()

↓

strptime()

↓

datetime

↓

strftime()

↓

texte affiché
```

---

### Exercice 7

Parmi les situations suivantes, lesquelles utiliseraient plusieurs outils ensemble ?

- Réservation en ligne : `oui`
- Gestion d'abonnement : `oui`
- Calculatrice simple : `non`
- Agenda : `oui`
- Livraison : `oui`

---

### Exercice 8

1. Pourquoi les applications utilisent-elles souvent plusieurs outils de date et heure ensemble ?
    - parce qu'une application doit souvent lire une date, la manipuler, effectuer des calculs puis l'afficher à l'utilisateur
2. Quel est le rôle de `strptime()` dans une application réelle ?
    - convertir une date saisie sous forme de texte en objet `datetime`
    - permettre ensuite les calculs et comparaisons
3. Quel est le rôle de `strftime()` dans une application réelle ?
    - convertir un objet `datetime` en texte lisible pour l'utilisateur
    - personnaliser l'affichage des dates et heures
4. Quel est le rôle de `timedelta` dans une application réelle ?
    - représenter une durée
    - calculer une échéance
    - déterminer le temps restant avant un événement
    - ajouter ou soustraire du temps à une date
5. Cite un projet personnel où tu pourrais utiliser les quatre outils ensemble.
    ```text
    Rabbit Manager
    ```

    - date de naissance
    - âge des lapins
    - durée de gestation
    - dates d'accouplement
    - affichage des échéances
