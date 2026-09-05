# Exercices

### Exercice 1

Crée un datetime actuel avec :

```text
Europe/Brussels
```

Puis affiche-le.

---

### Exercice 2

Crée un datetime actuel avec :

```text
Africa/Porto-Novo
```

Puis affiche-le.

---

### Exercice 3

Crée un datetime actuel avec :

```text
UTC
```

Puis affiche-le.

---

### Exercice 4

Complète :

| Élément             | Rôle |
| ------------------- | ---- |
| `ZoneInfo`          |      |
| `"UTC"`             |      |
| `"Europe/Brussels"` |      |
| Aware Datetime      |      |

---

### Exercice 5

Associe :

| Besoin                          | Outil |
| ------------------------------- | ----- |
| Ajouter un fuseau à un datetime |       |
| Représenter Bruxelles           |       |
| Représenter Porto-Novo          |       |
| Représenter UTC                 |       |

---

### Exercice 6

Complète :

```text
datetime.now()

↓

Naive Datetime
```

et

```text
datetime.now(ZoneInfo(...))

↓

...
```

---

### Exercice 7

Parmi les situations suivantes, lesquelles nécessitent un fuseau horaire ?

* Réservation de vol
* Réunion internationale
* Réseau social mondial
* Calculatrice
* Agenda partagé

Réponds par :

```text
oui
```

ou

```text
non
```

---

### Exercice 8

Réponds avec tes propres mots :

1. Quel est le rôle de `ZoneInfo` ?
2. Pourquoi utiliser un nom comme `"Europe/Brussels"` ?
3. Quelle différence existe entre un datetime naïf et un datetime utilisant `ZoneInfo` ?
4. Cite deux fuseaux horaires valides.
5. Dans quel type de projet utiliserais-tu `ZoneInfo` ?