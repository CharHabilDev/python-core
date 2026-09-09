# Exercices

## Exercice 1

Importe `defaultdict`.

```python
from collections import defaultdict
```

---

## Exercice 2

Complète :

| Élément       | Rôle |
| ------------- | ---- |
| `collections` | module contenant des structures de données    |
| `defaultdict` | dictionnaire créant automatiquement une valeur par défaut pour les clés absentes    |

---

## Exercice 3

Complète :

```text
defaultdict

↓

initialisation automatique des clés
```

---

## Exercice 4

Associe :

| Situation                                   | Outil         |
| ------------------------------------------- | ------------- |
| Créer automatiquement une valeur par défaut | `defaultdict` |
| Grouper des données                         | `defaultdict` |
| Éviter les KeyError                         | `defaultdict` |
| Initialiser automatiquement une clé         | `defaultdict` |

---

## Exercice 5

Parmi les situations suivantes, lesquelles pourraient utiliser `defaultdict` ?

* Comptage de votes : `oui`
* Analyse de texte : `oui`
* Calendrier : `non `
* Regroupement d'étudiants : `oui`
* Gestion de catégories : `oui`

---

## Exercice 6

Complète :

```text
clé absente

↓

defaultdict

↓

valeur par defaut
```

---

## Exercice 7

Réponds avec tes propres mots :

1. Quel est le rôle de `defaultdict` ?
    - créer une valeur par defaut lorsqu'une clé est absente
2. Quel problème résout-il ?
    - `keyError` (évite les erreurs liées aux clés inexistantes)
3. Pourquoi est-il utile ?
    - il évite de devoir créer manuellement les valeurs avant de les utiliser
4. Cite deux cas d'utilisation réels.
    - regroupement d'étudiants par classe
    - classement de produits par catégorie
5. Dans quel projet personnel pourrais-tu utiliser `defaultdict` ?
    - Event Manager (événements regroupés par mois)