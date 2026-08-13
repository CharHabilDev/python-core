'''
## Exercice 1

Crée une fonction :

```python
compte_a_rebours(n)
```

qui affiche :

```text
5
4
3
2
1
Décollage !
```

pour :

```python
compte_a_rebours(5)
```
'''

def compte_a_rebours(n):
    if n == 0:
        print("Décollage !")
        return
    
    print(n) 
    compte_a_rebours(n-1)

compte_a_rebours(5)



'''
## Exercice 2

Crée une fonction récursive :

```python
somme(n)
```

qui retourne :

```text
1 + 2 + 3 + ... + n
```
'''

def somme(n):
    if n <= 0:    
        return 0
    return n + somme(n - 1)

print(somme(5)) # 15


'''
## Exercice 3

Crée une fonction récursive :

```python
puissance(base, exposant)
```
'''

def puissance(base, exposant):

    if exposant == 0:
        return 1

    return base * puissance(base, exposant-1)


print(puissance(2,8)) # 256



'''
## Exercice 4

Crée une fonction récursive :

```python
compter_lettres(mot)
```

qui retourne le nombre de caractères d'une chaîne.
'''

def compter_lettres(mot):
    if not mot:
        return 0
    return 1 + compter_lettres(mot[1:])

print(compter_lettres('python')) # 6



'''
## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une fonction récursive ?
    # c'est une fonction qui s'appelle elle même
2. Pourquoi faut-il un cas d'arrêt ?
    # pour éviter une récursion infinie qui provoque `RecursionError`
3. Que se passe-t-il sans cas d'arrêt ?
    # une RecursionError` 
4. Quelle différence vois-tu entre une boucle et une récursion ?
    # Une boucle utilise for ou while, tandis qu'une récursion utilise des appels successifs de la même fonction.
5. Dans quels types de problèmes la récursion est-elle particulièrement utile ?
    - arbres (tree structures)
    - dossiers et sous-dossiers
    - algorithmes de recherche
    - parcours de structures imbriquées
'''