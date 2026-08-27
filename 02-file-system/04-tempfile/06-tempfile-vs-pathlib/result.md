# Exercises

## Exercice 1

Complète le tableau :

| Critère | Fichier manuel | tempfile |
|----------|----------|----------|
| Nom unique | non garanti |garanti |
| Nettoyage automatique | non | oui |
| Gestion des erreurs | non | oui |

---

## Exercice 2

Pour chaque situation, indique :

```text
Manuel
tempfile
```

### Situation A

Fichier intermédiaire de conversion PDF. : `tempfile`

### Situation B

Configuration de l'application. : `Manuel`

### Situation C

Cache temporaire. : `tempfile`

### Situation D

Base de données principale. : `Manuel`

### Situation E

Extraction temporaire d'une archive. : `tempfile`

---

## Exercice 3

Explique pourquoi cette approche peut être risquée :

```python
Path("temp.txt")
```
- pas de garantie pour le nettoyage
- risque d'écrasement du fichier s'il existe déjà
- risque de conflit si plusieurs programmes utilisent temp.txt
---

## Exercice 4

Cite deux avantages de `tempfile`.
- Unicité garantie des noms 
- Nettoyage automatique et sécurisé
---

## Exercice 5

Cite deux situations où un fichier manuel est préférable.
- la persistance des données
- le contrôle total du chemin et du nom
---

## Exercice 6

Complète :

```text
Fichier temporaire
↓
volatile

Fichier permanent
↓
persistant

Nom unique
↓
généré automatiquement
```

---

## Exercice 7

Tu développes une application qui :

1. génère un rapport ;
2. crée plusieurs fichiers intermédiaires ;
3. produit un PDF final.

Quels fichiers devraient être temporaires et lesquels devraient être permanents ?

```txt
Fichiers intermédiaires
↓
temporaires

PDF final
↓
permanent
```
---

## Exercice 8

Réponds avec tes propres mots :

1. Pourquoi `tempfile` est-il plus sûr ?
    - parce qu'il garantit le nettoyage automatique et les noms uniques
2. Quel problème résout-il principalement ?
    - problème de la gestion non sécurisé des dossiers et fichiers éphémères
3. Quand préférerais-tu créer un fichier manuellement ?
    - quand j'ai besoin de l'utiliser plus tard, ou pour le concerver
4. Pourquoi les fichiers oubliés peuvent-ils devenir un problème ?
    - occupation inutile du disque
    - accumulation de fichiers
    - confusion
    - ralentissement de certaines opérations
5. Résume la différence entre `tempfile` et un fichier manuel en une phrase.
    - `tempfile` automatise la création de noms uniques et la suppression du fichier dès sa fermeture, là où un fichier manuel oblige à tout gérer sois-même