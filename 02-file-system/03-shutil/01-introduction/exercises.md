# Exercises

## Exercice 1

Importe le module `shutil`.

Affiche ensuite son type.

---

## Exercice 2

Affiche l'aide intégrée du module afin d'observer les fonctions qu'il contient.

Explore la sortie sans chercher à tout comprendre.

---

## Exercice 3

Parmi les opérations suivantes, indique celles qui semblent appartenir à `shutil` :

- Copier un fichier
- Obtenir le dossier courant
- Déplacer un dossier
- Lire une variable d'environnement
- Créer une archive
- Vérifier qu'un fichier existe

---

## Exercice 4

Associe chaque tâche au module le plus adapté :

| Tâche | Module |
|---------|---------|
| Construire un chemin | ? |
| Copier un fichier | ? |
| Obtenir le dossier courant | ? |
| Lire une variable d'environnement | ? |
| Supprimer un dossier complet | ? |
| Vérifier qu'un fichier existe | ? |

Modules disponibles :

```text
pathlib
os
shutil
```

---

## Exercice 5

Complète le tableau suivant :

| Module  | Rôle principal |
| ------- | -------------- |
| pathlib | ?              |
| os      | ?              |
| shutil  | ?              |

---

## Exercice 6

Pour chaque situation, choisis le module le plus adapté :

### Situation A

Tu veux créer le chemin :

```text
documents/cours/python/notes.txt
```

---

### Situation B

Tu veux connaître le dossier courant.

---

### Situation C

Tu veux copier un projet dans un dossier de sauvegarde.

---

### Situation D

Tu veux lire une variable d'environnement nommée :

```text
API_KEY
```

---

### Situation E

Tu veux supprimer un dossier contenant plusieurs sous-dossiers et fichiers.

---

## Exercice 7

Réponds avec tes propres mots :

1. Quel est le rôle principal de `shutil` ?
2. Pourquoi `shutil` est-il considéré comme un module de haut niveau ?
3. Quelle différence vois-tu entre `Path` et `shutil` ?
4. Quelle différence vois-tu entre `os` et `shutil` ?
5. Dans quel cas utiliserais-tu `shutil` dans un projet réel ?

---

## Exercice 8

Imagine que tu développes un script de sauvegarde automatique.

Explique brièvement comment :

- `pathlib`
- `os`
- `shutil`

pourraient travailler ensemble dans ce projet.

```

Ce chapitre est volontairement très théorique. Le but est de bien comprendre la place de `shutil` avant de commencer à copier ou déplacer de vrais fichiers dans le chapitre suivant. Une fois que `rmtree()` entre en scène, les exercices deviennent moins philosophiques et davantage "j'espère que tu avais une sauvegarde".
```