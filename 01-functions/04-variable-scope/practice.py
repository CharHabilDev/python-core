'''
## Exercice 1

Crée une fonction :

```python
def saluer():
```

À l'intérieur :

```python
nom = "Ali"
```

Affiche `nom` dans la fonction.

Puis essaye de l'afficher en dehors de la fonction.

Que se passe-t-il ?
'''

def saluer():
    nom = 'Ali'
    print(f"Salut {nom}")

#print(nom) # name 'nom' is not defined



'''
## Exercice 2

Crée :

```python
ville = "Cotonou"
```

Puis :

```python
def afficher_ville():
```

Affiche `ville`.

Teste la fonction.
'''

ville = 'Cotonou'

def afficher_ville():
    print(ville)

afficher_ville()


'''
## Exercice 3

Observe le résultat :

```python
nom = "Ali"

def afficher():
    nom = "Fatima"
    print(nom)

afficher()
print(nom)
```

Explique avec tes propres mots pourquoi les deux affichages sont différents.
'''

nom = "Ali"

def afficher():
    nom = "Fatima"
    print(nom)

afficher()
print(nom)

# les deux affichages n'affichent pas la même chose puisque le nom défini dans la fonction 
# est une variable locale différente de la variable nom définie hors de la fonction qui est une variable globale.


'''
## Exercice 4

Crée :

```python
compteur = 0
```

Puis une fonction :

```python
incrementer()
```

qui utilise :

```python
global compteur
```

et ajoute 1 à chaque appel.

Teste plusieurs appels.
'''

compteur = 0

def incrementer():
    global compteur

    compteur += 1 

incrementer()
incrementer()
incrementer()

print(compteur) # 3


'''
## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une variable locale ?
    # C'est une variable qui a une portée limitée à la fonction dans laquelle elle est définie.
2. Qu'est-ce qu'une variable globale ?
    # C'est une variable qui peut être utilisée partout dans le programme.
3. Pourquoi faut-il limiter l'utilisation de `global` ?
    # rend le code difficile à comprendre / maintenance
    # complique les tests unitaires
4. Pourquoi les paramètres sont-ils considérés comme des variables locales ?
    # parce qu'on ne peut pas les utiliser ailleurs que dans la fonction
'''