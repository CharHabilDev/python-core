from pathlib import Path

print("\n### Exercice 1")

path1 = Path("documents/notes.txt")

print(f"Nom complet : {path1.name}")
print(f"Nom : {path1.stem}")
print(f"Extension : {path1.suffix}") # difference avec suffixes
print(f"Dossier parent : {path1.parent}") 


print("\n### Exercice 2")

path2 = Path("images/photo.jpg")
print(f'Les parties du chemin : {path2.parts}')


print("\n### Exercice 3")

path3 = Path("fichier_inexistant.txt")
print(f"le fichier `{path3}` existe ? {path3.exists()}")


print('\n### Exercice 4')

path4 = Path('../01-introduction')
print(f"Le chemin {path4} est un fichier ? {path4.is_file()}")

path5 = Path('../01-introduction/practice.py')
print(f"Le chemin {path5} est un fichier ? {path5.is_file()}")


print('\n### Exercice 5')

path6 = Path('../02-properties-and-navigation/')
print(f'Le chemin {path6} est un dossier ? {path6.is_dir()}')

path7 = Path('exercises.md')
print(f'Le chemin {path7} est un dossier ? {path7.is_dir()}')


print('\n### Exercice 6')
"""
1. Différence entre `.name` et `.stem` ?
    # `.name` affiche le nom du fichier avec l'extension, alors que `stem` n'affiche pas l'extension
2. Que retourne `.suffix` ?
    # `.suffix` affiche l'extension d'un fichier
3. Que retourne `.parent` ?
    # `.parent` retour le dossier parent
4. Que contient `.parts` ?
    # `.parts` decompose le chemin en plusieurs parties (dossier, dossier, ..., fichier.extension)
5. Différence entre `.exists()`, `.is_file()` et `.is_dir()` ?
    # `.exists()` vérifie qu'un chemin existe
    # `.is_file()` vérifie qu'un chemin est un fichier
    # `.is_dir()` vérifie qu'un chemin est un dossier
"""