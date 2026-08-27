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

### Situation B

Base de données principale d'une application.

### Situation C

Extraction d'une archive ZIP contenant 500 fichiers.

### Situation D

Création d'un rapport intermédiaire avant génération du PDF final.

### Situation E

Stockage permanent des documents d'un utilisateur.

---

## Exercice 2

Complète :

| Situation                      | Outil |
| ------------------------------ | ----- |
| Un seul fichier temporaire     | ?     |
| Plusieurs fichiers temporaires | ?     |
| Données permanentes            | ?     |

---

## Exercice 3

Parmi les opérations suivantes, lesquelles sont de bons candidats pour `tempfile` ?

* conversion PDF
* cache temporaire
* photos utilisateur
* tests automatisés
* extraction ZIP
* sauvegarde définitive

---

## Exercice 4

Explique pourquoi un dossier temporaire est souvent préférable à plusieurs fichiers temporaires séparés.

---

## Exercice 5

Associe :

| Cas réel               | Outil le plus adapté |
| ---------------------- | -------------------- |
| Téléchargement unique  | ?                    |
| Projet de test complet | ?                    |
| Conversion d'image     | ?                    |
| Extraction ZIP         | ?                    |

---

## Exercice 6

Complète :

```text
TemporaryFile()
↓
...

TemporaryDirectory()
↓
...

Données permanentes
↓
...
```

---

## Exercice 7

Tu développes une application qui :

1. télécharge un ZIP ;
2. l'extrait ;
3. analyse les fichiers ;
4. produit un rapport final.

Quel(s) outil(s) `tempfile` utiliserais-tu et pourquoi ?

---

## Exercice 8

Réponds avec tes propres mots :

1. Quel cas d'utilisation te paraît le plus intéressant ?
2. Quand éviterais-tu absolument `tempfile` ?
3. Pourquoi les tests utilisent-ils souvent des dossiers temporaires ?
4. Quelle différence entre une donnée temporaire et une donnée permanente ?
5. Si tu développes un outil de sauvegarde, où utiliserais-tu `tempfile` ?