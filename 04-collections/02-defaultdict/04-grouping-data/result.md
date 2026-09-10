# Exercices

## Exercice 1

Complète :

```text
clé absente
↓
defaultdict(list)
↓
[]
↓
append(valeur)
```

---

## Exercice 2

Associe :

| Situation              | Factory |
| ---------------------- | ------- |
| Dépenses par catégorie | `list`       |
| Étudiants par classe   | `list`       |
| Événements par mois    | `list`       |
| Lapins par race        | `list`       |

---

## Exercice 3

Complète :

```text
Catégorie
↓
Food
↓
[]
↓
[15]
↓
[15, 20]
```

---

## Exercice 4

Réponds avec tes propres mots :

1. Pourquoi `defaultdict(list)` est-il utile pour le regroupement ?
    - il permet d'ajouter directement des valeurs à une catégorie sans devoir créer la liste manuellement.
2. Quel problème évite-t-il ?
    - evite de vérifier si la clé existe avant un ajout
3. Cite deux exemples réels de regroupement.
    - événements par mois
    - médicaments par catégorie
4. Dans quel projet personnel pourrais-tu regrouper des données ?
    - Rabbit Manager
    - Expense Analyzer
5. Pourquoi cette technique est-elle fréquente dans les applications ?
    - parce qu'elle simplifie le code et évite les vérifications répétitives.