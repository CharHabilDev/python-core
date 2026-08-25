import platform


print("### Exercice 1")
print(f"Affiche le nom du système d'exploitation : {platform.system()}")


print('\n### Exercice 2')
print(f"Affiche la version du système d'exploitation : {platform.release()}")


print('\n### Exercice 3')
print(f"Affiche les informations détaillées du système.")
print(platform.platform())


print('\n### Exercice 4')
print(f"Affiche l'architecture de la machine : {platform.machine()}")


print('\n### Exercice 5')
print(f"Affiche la version de Python utilisée : {platform.python_version()}")


print('\n### Exercice 6')
print(f"Affiche le nom de l'interpréteur Python utilisé : {platform.python_implementation()}")


print('\n### Exercice 7')

print("=== SYSTEM REPORT ===\n")
print(f"{'System':15}: {platform.system()}")
print(f"{'Release':15}: {platform.release()}")
print(f"{'Machine':15}: {platform.machine()}")
print(f"{'Python':15}: {platform.python_version()}")
print(f"{'Interpreter':15}: {platform.python_implementation()}")


"""
### Exercice 8

1. À quoi sert le module `platform` ?
    # le module `platform` sert de complement au module `os` pour avoir plus d'infos sur le système
2. Que retourne `platform.system()` ?
    # le système d'exploitation
3. Que retourne `platform.machine()` ?
    # l'architecture matérielle de la machine.
4. Pourquoi connaître la version de Python peut être utile ?
    # parceque certains modules (bibliothèque externes) ne fonctionne qu'avec une version précise ou à partir d'une version jusqu'à une version de python
    - compatibilité du code
    - débogage
    - installation de dépendances
5. Quelle différence entre `os.name` et `platform.system()` ?
    # `os.name` retourne la famille du système alors que `platform.system()` retourne le nom réel du système
"""