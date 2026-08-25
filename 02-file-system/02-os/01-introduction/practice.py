print('\n### Exercice 1')
import os

print(f"Nom du système : {os.name}")


print('\n### Exercice 2')
print(f"Dossier courant : {os.getcwd()}")


print('\n### Exercice 3')
print('Les éléments du dossier courant : ')
print(os.listdir())

print(f'Les éléments du dossier `02-environment-variables`')
print(os.listdir('../02-environment-variables'))


print("\n### Exercice 4")
print('Création de du dossier `test` : ')
try:
    os.mkdir('test')
    print("Création avec succès.")
except FileExistsError:
    print("Le dossier existe déjà.")


print('\n### Exercice 5')
print('Suppression du dossier `test` : ')
try:
    os.rmdir('test') 
    print("Suppression avec succès.")
except FileNotFoundError:
    print("Erreur : Le dossier n'exite pas.")


print("\n### Exercice 6")
"""
1. À quoi sert le module `os` ?
    # Le module `os` sert à interagir avec le système d'exploitation de l'ordinateur.
2. Que retourne `os.name` ?
    # Le système d'exploitation 
        - `posix` pour linux et mac
        - `nt` pour windows
3. Que retourne `os.getcwd()` ?
    # Le chemin abosolue du dossier courant
4. Que retourne `os.listdir()` ?
    # La liste des éléments du dossier courant
5. Différence principale entre `os` et `pathlib` ?
    # `os` utilise les chaînes de caractères (str) alors que `pathlib` crée et utilise les objets
"""