'''
## Exercice 1

Crée une fonction classique :

```python
def carre(nombre):
    return nombre * nombre
```

Puis crée son équivalent avec une lambda.

Teste :

```python
carre(5)
```
'''

def carre(nombre):
    return nombre * nombre

carre_lambda = lambda nombre: nombre * nombre

print(carre(5))
print(carre_lambda(5))



'''
## Exercice 2

Crée une lambda qui additionne deux nombres.

Teste :

```python
addition(10, 5)
```
'''

addition = lambda a, b: a + b

print(addition(10,5))


'''
## Exercice 3

Soit :

```python
noms = [
    "Omar",
    "Ali",
    "Fatima",
    "Youssouf"
]
```

Utilise `sorted()` pour trier la liste selon la longueur des noms.

Indice :

```python
key=lambda ...
```
'''
noms = [
    "Omar",
    "Ali",
    "Fatima",
    "Youssouf"
]

sort_noms = sorted(
    noms, 
    key=lambda nom: len(nom)
)
print(sort_noms)



'''
## Exercice 4

Soit :

```python
produits = [
    {"nom": "SSD", "prix": 100},
    {"nom": "Écran", "prix": 250},
    {"nom": "Clavier", "prix": 50}
]
```

Utilise `max()` avec une lambda pour récupérer le produit le plus cher.

Affiche le résultat.
'''

produits = [
    {"nom": "SSD", "prix": 100},
    {"nom": "Écran", "prix": 250},
    {"nom": "Clavier", "prix": 50}
]
max_product = max(
    produits, 
    key=lambda product: product['prix']
)
print(max_product)


'''
## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une fonction lambda ?
    # c'est une fonction anonyme écrite sur une seule ligne et utilisée pour les traitements simples
2. Quelle différence principale existe entre une fonction classique et une lambda ?
    # Une fonction classique est définie avec def et peut contenir plusieurs instructions, 
    # tandis qu'une lambda est une fonction anonyme limitée à une seule expression.
3. Dans quels cas utiliserais-tu une lambda ?
    # pour un traitement éphémère
        - avec sorted()
        - avec max()
        - avec min()
        - avec map() et filter()
4. Pourquoi évite-t-on les lambdas pour des traitements complexes ?
    # Les lambdas sont limitées à une seule expression et deviennent rapidement difficiles à lire lorsqu'elles contiennent une logique complexe.
    # tests unitaire impossible 
    
'''