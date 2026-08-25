import os

dossier_initial = os.getcwd()

print("### Exercice 1")
print(f"Dossier courant : {os.getcwd()}")


print("\n### Exercice 2")
try:
    os.mkdir("test_directory")
except FileExistsError:
    print("`test_directory` existe déjà.")

print(f"Dossier courant : {os.getcwd()}") #.../03-working-directory

os.chdir('test_directory') # Change directory 

print(f"Dossier courant : {os.getcwd()}") #.../03-working-directory/test_directory


print("\n### Exercice 3")
# Dossier courant
    #.../03-working-directory/test_directory

try:
    os.mkdir('data')
except FileExistsError:
    print("`data` existe déjà.")

print("Contenu du dossier courant : ")
print(os.listdir()) # os.listdir(os.getcwd())


print("\n### Exercice 4")
# Sauvegarde en haut, car dossier déjà changée

# Navigue vers test_directory: depuis le haut
chemin_test_directory = os.getcwd()

#Puis retourne au dossier initial.
os.chdir(dossier_initial)

print("Affiche les deux chemins.")

print(f"Dossier initial : {dossier_initial}")
print(f"Dossier courant : {chemin_test_directory}")
       

print("\n### Exercice 5")
print(os.listdir())

os.chdir("test_directory")

print(os.listdir())


print("\n### Exercice 6")
#Nettoie les dossiers créés pendant les exercices.
# aller au dossier test
if chemin_test_directory != os.getcwd():
    os.chdir(chemin_test_directory)

# suppression de data
os.rmdir("data")

# Aller au dossier initial si ce n'est pas le dossier courant
if dossier_initial != os.getcwd():
    os.chdir(dossier_initial) # Change directory 

# suppression de test_directory
os.rmdir('test_directory')


print("\n### Exercice 7")
"""
1. À quoi sert `os.getcwd()` ?
    # À afficher le dossier courant
2. À quoi sert `os.chdir()` ?
    # `os.chdir()` = Change Directory et sert à naviger vers un dossier
3. Pourquoi le dossier courant est-il important ?
    # pour ne pas exécuter une action qui ne devrait pas être exécuté à ce endroit
4. Pourquoi certaines erreurs `FileNotFoundError` sont-elles liées au dossier courant ?
    # parceque le fichier/dossier n'existe pas dans le dossier courant
5. Pourquoi est-il souvent utile de sauvegarder le dossier initial avant de le modifier ?
    # parceque l'on peut vite revenir à ce dossier avant d'executer une action qui concerne ce dossier
"""