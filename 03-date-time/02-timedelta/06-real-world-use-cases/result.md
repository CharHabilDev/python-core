## Exercices

### Exercice 1

Pour chaque situation, indique si tu utiliserais principalement :

```text
date
datetime
timedelta
```

- Anniversaire : `date`
- Durée d'un abonnement : `timedelta`
- Heure d'un rendez-vous : `datetime`
- Temps écoulé depuis une connexion : `timedelta`
- Jour férié : `date`

---

### Exercice 2

Associe :

| Situation              | Objet principal |
| ---------------------- | --------------- |
| Réservation d'hôtel    | `datetime`      |
| Calcul d'âge           | `timedelta`     |
| Période d'essai        | `timedelta`     |
| Mesure d'une exécution | `timedelta`     |

---

### Exercice 3

Complète :

| Cas réel     | Utilisation |
| ------------ | ----------- |
| Expiration   |`timedelta`             |
| Livraison    |`datetime`             |
| Notification |`datetime`             |
| Statistiques |`timedelta`             |

---

### Exercice 4

Parmi les situations suivantes, lesquelles nécessitent un calcul de durée ?

- Temps de téléchargement : `oui`
- Date de naissance : `non`
- Temps de trajet : `oui`
- Abonnement : `oui`
- Nom d'utilisateur : `non`

---

### Exercice 5

Associe :

| Besoin                    | Opération                       |
| ------------------------- | ------------------------------- |
| Obtenir une date future   | `date/datetime + timedelta`     |
| Obtenir une durée écoulée | `date/datetime - date/datetime` |
| Afficher un délai         | `timedelta`                     |
| Mesurer une performance   | `timedelta.total_seconds()`     |

---

### Exercice 6

Complète :

```text
date

+

timedelta

↓

nouvelle date
```

et

```text
date

-

date

↓

timedelta
```

---

### Exercice 7

Réponds brièvement :

1. Pourquoi `timedelta` est-il important dans les applications ?
    - parcequ'il permet de faire des opérations complexe comme une échéance
2. Cite trois domaines qui utilisent des durées.
    - jeu vidéo
    - finance
    - logistique
3. Pourquoi mesurer des temps d'exécution ?
    - pour comparer l'efficacité et la rapidité de deux tâche
4. Pourquoi calculer une date future ?
    - pour planifier des rappels ou événements
    - fixer une date de fin
5. Quel exemple de projet personnel pourrait utiliser `timedelta` ?
    - un gestionnaire de révisions

### Exercice 8

#### Gestionnaire de tâches

- calculer les jours restants avant une échéance ;
- afficher les tâches en retard.

#### Rabbit Manager

- calculer la durée de gestation ;
- calculer l'âge d'un lapin.

#### Projet ferme

- suivi des cycles de reproduction ;
- planification des récoltes ;
- rappels de vaccination.

#### Gestionnaire de révisions

- calcul de la prochaine révision ;
- temps restant avant une révision.

#### Expense Analyzer

- statistiques mensuelles ;
- dépenses sur les 30 derniers jours ;
- comparaison de périodes.
