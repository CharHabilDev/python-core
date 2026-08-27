# Exercises

## Exercice 1

Pour chaque situation, indique :

```text
TemporaryFile()
TemporaryDirectory()
Aucun
```
### Situation A

Téléchargement d'un fichier PDF avant analyse. 
- TemporaryFile()

### Situation B

Base de données principale d'une application.
- Aucun

### Situation C

Extraction d'une archive ZIP contenant 500 fichiers.
- TemporaryDirectory()

### Situation D

Création d'un rapport intermédiaire avant génération du PDF final.
- TemporaryFile()

### Situation E

Stockage permanent des documents d'un utilisateur.
- Aucun 

---

## Exercice 2

Complète :

| Situation                      | Outil |
| ------------------------------ | ----- |
| Un seul fichier temporaire     |TemporaryFile() |
| Plusieurs fichiers temporaires |TemporaryDirectory() |
| Données permanentes            |Aucun     |

---

## Exercice 3

Parmi les opérations suivantes, lesquelles sont de bons candidats pour `tempfile` ?

* conversion PDF : `oui`
* cache temporaire : `oui`
* photos utilisateur : `non`
* tests automatisés : `oui`
* extraction ZIP : `oui`
* sauvegarde définitive : `non`

---

## Exercice 4

Explique pourquoi un dossier temporaire est souvent préférable à plusieurs fichiers temporaires séparés.

- cela permet de regrouper les fichiers et ainsi de faire le traitement en même temps
- un seul nettoyage et tout le dossier disparaît

---

## Exercice 5

Associe :

| Cas réel               | Outil le plus adapté |
| ---------------------- | -------------------- |
| Téléchargement unique  | TemporaryFile()      |
| Projet de test complet | TemporaryDirectory() |
| Conversion d'image     | TemporaryFile()      |
| Extraction ZIP         | TemporaryDirectory() |

---

## Exercice 6

Complète :

```text
TemporaryFile()
↓
un fichier temporaire

TemporaryDirectory()
↓
un espace de travail temporaire

Données permanentes
↓
pas tempfile
```

---

## Exercice 7

Tu développes une application qui :

1. télécharge un ZIP ;
2. l'extrait ;
3. analyse les fichiers ;
4. produit un rapport final.

Quel(s) outil(s) `tempfile` utiliserais-tu et pourquoi ?
`TemporaryDirectory()`

---

## Exercice 8

Réponds avec tes propres mots :

1. Quel cas d'utilisation te paraît le plus intéressant ?
    - téléchargement temporaire
2. Quand éviterais-tu absolument `tempfile` ?
    - pour des données permanentes
3. Pourquoi les tests utilisent-ils souvent des dossiers temporaires ?
    ```text
    Créer un environnement de test isolé
    ↓
    Tester
    ↓
    Tout supprimer automatiquement
    ```
4. Quelle différence entre une donnée temporaire et une donnée permanente ?
    - une donnée temporaire est supprimée après son utilisation alors qu'une une donnée permanente n'est pas supprimée
5. Si tu développes un outil de sauvegarde, où utiliserais-tu `tempfile` ?
    - compression et création d'archive