from pathlib import Path

# Exercices

print("\n### Exercice 1")

# Crée un dossier de test contenant plusieurs fichiers et dossiers.

# 1. chemin du dossier racine du test
dossier_test = Path.cwd() / "exercice_pathlib"

# 2. Créeation du dossier principal
dossier_test.mkdir(exist_ok=True)

# 3. Structure des sous-dossiers
sous_dossiers = [
    dossier_test / "images",
    dossier_test / "documents" / "textes",
    dossier_test / "sauvegardes"
]

# 4. Créeation des sous-dossiers
for dossier in sous_dossiers:
    dossier.mkdir(parents=True, exist_ok=True)

# 5. Les fichiers à créer
fichiers = [
    dossier_test / "readme.md",
    dossier_test / "images" / "photo1.png",
    dossier_test / "images" / "logo.jpg",
    dossier_test / "documents" / "textes" / "notes.txt",
    dossier_test / "documents" / "textes" / "rapport.docx",
    dossier_test / "sauvegardes" / "data.csv"
]

# 6. Créeation des fichiers vides
for fichier in fichiers:
    fichier.touch(exist_ok=True)

print(f"Structure de test créée avec succès dans : {dossier_test}")


print("\n### Exercice 2")
print("# Affiche tous les éléments présents dans ce dossier.")

if dossier_test.exists():
    print(f"--- Contenu de {dossier_test.name} ---") # Pas jolie à voir

    for element in dossier_test.iterdir():
        if element.is_dir():
            print("Dossier : ", element)
        else:
            print("Fichier : ", element)
else:
    print("Le dossier n'existe pas.")


print("\n### Exercice 3")
print("# Affiche uniquement les fichiers.")
if dossier_test.exists():
    print(f"--- Contenu de {dossier_test.name} ---") # Pas jolie à voir

    for element in dossier_test.iterdir():
        if element.is_file():
            print("Fichier : ", element)
else:
    print("Le dossier n'existe pas.")


print("\n### Exercice 4")
print("Affiche uniquement les dossiers.")

if dossier_test.exists():
    print(f"--- Contenu de {dossier_test.name} ---") # Pas jolie à voir

    for element in dossier_test.iterdir():
        if element.is_dir():
            print("Dossier : ", element)
else:
    print("Le dossier n'existe pas.")


print("\n### Exercice 5")
print("""Recherche tous les fichiers :
```text
.txt
```
du dossier.""")


for element in dossier_test.glob("*.txt"):
    print(element)


print("\n### Exercice 6")
for element in dossier_test.rglob("*.txt"):
    print(element)



print("\n### Exercice 7")


"""
1. À quoi sert `iterdir()` ?
    # `iterdir()` sert à parcourir tous les élements d'un dossier
2. Différence entre `glob()` et `rglob()` ?
    # `glob()` les recherches de s'arrêtent dans le dossier courant alors que `rglob()` vérifie dans les sous dossiers
3. Que signifie `*.txt` ?
    # `*.txt` : 
        - `*` : n'importe quelle suite de caractères
        - `.txt` impose que le nom du fichier se termine exactement par ces caractères.
4. Comment vérifier qu'un élément est un fichier ?
    # element.is_file()
5. Comment vérifier qu'un élément est un dossier ?
    # element.is_dir()
6. Dans quel cas utiliserais-tu une recherche récursive ?
    # si je recherche un élement qui peut se retrouver dans les sous dossiers
"""