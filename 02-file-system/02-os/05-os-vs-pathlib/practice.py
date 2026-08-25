import os
from pathlib import Path


print("### Exercice 1")
print("Création du chemin `documents/notes.txt`: \nAvec : ")

print("os")
os_path = os.path.join(
    'documents',
    'notes.txt'
)

print('pathlib')
path = Path("documents") / 'notes.txt'

print(os_path)
print(path)


print("\n### Exercice 2")
print("Vérifie l'existence d'un fichier :\nAvec : ")

print("os")
print("'README.md' existe ?", os.path.exists('README.md'))

print('pathlib')
print("'README.md' existe ?", Path('README.md').exists())


print("\nExercice 3")
print("Vérifie qu'un élément est un fichier :\nAvec: ")
print("os")
print(f"`exercises.md` est un fichier ? {os.path.isfile('exercises.md')}")
print('pathlib')
print(f"`exercises.md` est un fichier ? {Path('exercises.md').is_file()}")


print("\nExercice 4")
print("Vérifie qu'un élément est un dossier :\nAvec: ")
print("os")
print(f"`../04-system-information` est un dossier ? {os.path.isdir('../04-system-information')}")
print('pathlib')
print(f"`../04-system-information` est un dossier ? {Path('../04-system-information').is_dir()}")


print("\n### Exercice 5")
print("Réécris ce code utilisant os avec pathlib :")

path = Path("images") / 'photo.jpg'
print(path.exists())

print("\n### Exercice 6")
path = Path("documents") / "cours" / "python" / "notes.txt"
print(path)


"""
## Exercice 7

1. Pourquoi `pathlib` a-t-il été introduit ?
    - moderniser python
    - éliminer les sythaxes imbriquées comme `os.path.join`
2. Quelle différence principale vois-tu entre `os.path` et `Path` ?
    # `os.path` utilise les chaines de caractères alors que `Path` utilise les objets
3. Dans quel cas utiliserais-tu encore `os` ?
    # Pour manipuler ou avoir des informations venant du système d'exploitation
4. Pourquoi beaucoup de projets modernes préfèrent-ils `pathlib` ?
    # Parceque `pathlib` est plus simple et lisible
5. Quel module utiliserais-tu pour gérer des variables d'environnement ?
    # le module `os`
"""