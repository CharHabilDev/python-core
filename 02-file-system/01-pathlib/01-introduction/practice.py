### Exercice 1

from pathlib import Path


### Exercice 2
fichier = Path("README.md")
print(fichier)


### Exercice 3
print('Dossier courant : ', Path.cwd())


### Exercice 4
print(f"Dossier personnel : {Path.home()}")


### Exercice 5
path = Path('documents')/'notes.txt'

print(path)



### Exercice 6

# 1. Qu'est-ce qu'un objet `Path` ?
    # Un objet Path représente et manipule un chemin vers un fichier ou un dossier.
# 2.    
    # le chemain relatif indique l'accès à un dossier en partant du dossier parent/courant
    # alors que le chemain absolue donne l'addresse complet du fichier ou dossier en partant de
    # la racine du disque
# 3. À quoi sert `Path.cwd()` ?
    # sert à trouver le chemain absolue du dossier courant
# 4. À quoi sert `Path.home()` ?
    # sert à trouver le chemain absolue du dossier personnel de l'user
# 5. Pourquoi utiliser `/` plutôt que concaténer des chaînes ?
    # pour que le code fonctionne sur tous les systèmes d'explotation sans modification,
    # eviter les erreurs liés au slash,
    # créer un objet Path manipulable