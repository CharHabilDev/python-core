print("### Exercice 1")
"""
Importe `os`.
Affiche :
```python
os.getenv("HOME")
```
"""

import os

print(f"Environnement `HOME` : {os.getenv('HOME')}")



print("\n### Exercice 2")
"""
Affiche :
```python
os.getenv("USER")
```
ou
```python
os.getenv("USERNAME")
```
selon ton système.
"""

print(f"Variable d'environnement `USER` : {os.getenv('USER')}")
print(f"Variable d'environnement `USERNAME` : {os.getenv('USERNAME')}")



print("\n### Exercice 3")
"""
Affiche une variable inexistante :
```python
os.getenv("VARIABLE_INVENTEE")
```
Observe le résultat.
"""

print(f"Variable d'environnement `VARIABLE_INVENTEE` : {os.getenv('VARIABLE_INVENTEE')}")


print("\n### Exercice 4")
"""
Utilise :
```python
os.getenv(
    "VARIABLE_INVENTEE",
    "valeur_par_defaut"
)
```
Observe le résultat.
"""
print(f"Variable d'environnement `VARIABLE_INVENTEE` : {os.getenv('VARIABLE_INVENTEE', 'valeur_par_defaut')}")



print("\n### Exercice 5")
"""
Affiche les 10 premières variables d'environnement.
Indice conceptuel :
```text
os.environ
↓
dictionnaire
```
"""

print("Les 10 premières variables d'environnement :")
i = 0
for key, value in os.environ.items():
    if i < 10:
        print(key, value)
        i +=1



print("\n### Exercice 6")
"""
Vérifie si :
```text
HOME
```
existe dans les variables d'environnement.
"""
print("La variables d'environnement `HOME` Existe ? ", end='')
print("OUI" if 'HOME' in os.environ else "NON")



print("\n### Exercice 7")
"""
1. Qu'est-ce qu'une variable d'environnement ?
    # C'est une variable stockée par le système d'exploitation
2. À quoi sert `os.getenv()` ?
    # `os.getenv()` sert à afficher le contenu d'une variable d'environnement
3. Différence entre `getenv()` et `os.environ[]` ?
    # `getenv()` affiche `None` ou une valeur par défaut écrite si la variable d'environnement 
    # n'existe pas alors que `os.environ[]` soulève un KeyError
4. Pourquoi utiliser une valeur par défaut ?
    # pour éviter une erreur lorsqu'une variable n'existe pas et que cette variable est 
    # indispensable au fonctionnement du programme
5. Pourquoi stocker une clé API dans une variable d'environnement plutôt que dans le code ?
# pour la sécurité, car une clé API est généralement privée
"""