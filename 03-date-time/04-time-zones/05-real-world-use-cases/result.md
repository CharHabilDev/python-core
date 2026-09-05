# Exercises

### Exercice 1

Associe :

| Situation                       | Main Tool |
| ------------------------------- | --------- |
| User enters a date              |`strptime()`           |
| Show a date on screen           |`strftime()`           |
| Calculate a subscription period |`timedelta()`           |
| International meeting           |`ZoneInfo()`           |

---

### Exercice 2

Pour chaque projet, indique les outils qui pourraient être utilisés :

#### Hotel Reservation

- `strptime()` pour la convertion user_input
- `timedelta()` calcul du séjour
- `strftime()` affichage screen

#### Shared Calendar

- `datetime`
- `ZoneInfo()`
- `astimezone()`
- `strftime()`

#### Delivery Tracking

- `datetime`
- `timedelta`
- `strftime()`

---

### Exercice 3

Complète :

| Tool         | Role |
| ------------ | ---- |
| `datetime`   |un instant précis      |
| `timedelta`  |une durée      |
| `strftime()` |un datetime vers un str      |
| `strptime()` |un str vers un datetime      |
| `ZoneInfo()` |un fuseau horaire      |


---

### Exercice 4

Complète :

```text id="5r5phd"
User Input

↓

strptime

↓

datetime
```

et

```text id="j2lnmf"
datetime

↓

strftime

↓

text
```

---

### Exercice 5

Réponds avec tes propres mots :

1. Pourquoi les applications utilisent-elles souvent plusieurs outils de date et heure ensemble ?
        - l'utilisateur saisit du texte 
        - l'application le convertit 
        - elle effectue des calculs 
        - elle réaffiche le résultat
2. Quel est le rôle de `datetime` dans une application ?
    - représenter un instant précis dans le temps
3. Quel est le rôle de `timedelta` dans une application ?
    - représenter ou calculer une durée
4. Pourquoi les fuseaux horaires sont-ils importants ?
    - parce que les utilisateurs peuvent être situés dans différentes régions du monde
5. Dans quel projet personnel pourrais-tu utiliser `datetime`, `timedelta`, `strptime()`, `strftime()` et `ZoneInfo()` ensemble ?
    - gestionnaire de tâches 