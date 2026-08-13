'''
# Exercices

## Exercice 1

Crée un générateur :

```python
nombres()
```

qui produit :

```text
1
2
3
4
5
```

Utilise :

```python
for nombre in nombres():
    print(nombre)
```
'''

def nombres():
    for i in range(1, 6):
        yield i

for nombre in nombres():
    print(nombre)



'''
## Exercice 2

Crée un générateur :

```python
pairs(limite)
```

qui produit tous les nombres pairs jusqu'à `limite`.
'''

def pairs(limite):
    n = 2
    while n <= limite:
        yield n
        n += 2

    #for n in range(2, limite + 1, 2):
        #yield n

for nombre in pairs(10):
    print(nombre) 



'''
## Exercice 3

Crée un générateur :

```python
lettres(mot)
```

qui produit chaque caractère d'un mot.
'''

def lettres(mot):
    for c in mot:
        yield c

for lettre in lettres("python"):
    print(lettre)



'''
## Exercice 4

Utilise :

```python
next()
```

pour récupérer manuellement les valeurs produites par :

```python
nombres()
```
'''

def nombres():
    for i in range(1, 4):
        yield i

gen = nombres()

print(next(gen))
print(next(gen))
print(next(gen)) # 
print(next(gen)) # StopIteration



'''
## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'un générateur ?
    # Un générateur produit des valeurs une à une
2. Quelle différence existe entre `return` et `yield` ?
    # `return` retourne une valeur et arrête la fonction alors que `yield` met en pause la fonction
3. Pourquoi un générateur consomme-t-il moins de mémoire ?
    # parcequ'il ne retourne pas tous les données en même temps
4. Dans quels cas utiliserais-tu un générateur ?
    # traitements de logs
    # lecture de gros fichiers
    # data volumineux
    # système API
5. Que signifie l'erreur `StopIteration` ?
    # cette erreur signifie que le générateur a produit toutes ses valeurs et qu'il n'en reste plus.
'''