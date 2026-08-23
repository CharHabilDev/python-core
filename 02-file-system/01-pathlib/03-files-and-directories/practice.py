from pathlib import Path

root = Path('sandbox')

root.mkdir(exist_ok=True)

print("\n### Exercice 1")

path1 = root / 'test.txt'
path1.touch()
print(f" Fichier `test.txt` crée")


print("\n### Exercice 2")

path2 = root / "documents"
path2.mkdir(exist_ok=True)
print("Dossier `documents` crée")


print("\n### Exercice 3")

path3 = root / "cours/python/pathlib"
path3.mkdir(parents=True, exist_ok=True)
print(f"Le chemin {path3} a été créer")


print("\n### Exercice 4")

path4 = root / 'test.txt'
print(f"Fichier `test.txt` existe ? {path4.exists()}")


print("\n### Exercice 5")

path5 = root / 'test.txt'
path5.unlink(missing_ok=True)
print("Le fichier `test.txt` à été supprimer ? ", not path5.exists())  


print("\n### Exercice 6")
path6 = root / "dossier_vide"
path6.mkdir(exist_ok=True)

print(f"{path6} existe ? : {path6.exists()}")
print("suppression..............")
path6.rmdir()
print(f"{path6} existe ? : {path6.exists()}")


print("\n### Exercice 7")
'''
1. À quoi sert `touch()` ?
    # à créer un fichier
2. À quoi sert `mkdir()` ?
    # à créer un dossier
3. Pourquoi utiliser `exist_ok=True` ?
    # pour ne pas lever une exception si le dossier existe déjà
4. Pourquoi utiliser `parents=True` ?
    # pour ne pas lever d'exception si le(s) dossier(s) parents n'existe(nt) pas 
5. Différence entre `unlink()` et `rmdir()` ?
    # `unlink` supprime un fichier ou le lien du fichier alors que `rmdir` supprime un dossier vide.
6. Pourquoi `rmdir()` ne peut-il pas supprimer un dossier non vide ?
    # Pour éviter la suppression accidentelle des fichiers et sous-dossiers qu'il contient.
    # Python exige d'abord que le dossier soit vide afin de protéger les données.
'''