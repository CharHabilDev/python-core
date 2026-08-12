print('Exercice 1')
print('='*20)
'''
## Exercice 1

Crée une fonction :

```python
addition(*args)
```

qui additionne tous les nombres reçus.

Teste :

```python
addition(1, 2)
addition(1, 2, 3)
addition(1, 2, 3, 4, 5)
```
'''

def addition(*args):
    total = 0

    for nombre in args:
        total += nombre

    return total

print(addition(1, 2))
print(addition(1, 2, 3))
print(addition(1, 2, 3, 4, 5))



print('\n'+'='*20)
print('Exercice 2')
'''
## Exercice 2

Crée une fonction :

```python
afficher_notes(*args)
```

qui affiche chaque note sur une ligne.

Exemple :

```python
afficher_notes(12, 15, 18)
```
'''

def afficher_notes(*args):
    for note in args:
        print(note)

afficher_notes(12, 15, 18)


print('\n'+'='*20)
print('Exercice 3')
print('='*20)


'''
## Exercice 3

Crée une fonction :

```python
afficher_profil(**kwargs)
```

qui affiche :

```text
nom: Ali
age: 20
ville: Cotonou
```

pour n'importe quelles données reçues.
'''

def afficher_profil(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        

afficher_profil(nom='Ali', age=20, ville='Cotonou')


print('\n'+'='*20)
print('Exercice 4')
print('='*20)
'''
Crée une fonction :

```python
creer_utilisateur(username, **kwargs)
```

qui affiche :

```text
Username: charles
email: ...
age: ...
role: ...
```

Le `username` doit être obligatoire, les autres informations optionnelles.
'''

def creer_utilisateur(username, **kwargs):
    print(f"Username: {username}")
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")


creer_utilisateur('charles', email='charles@gmail.com')
print('---')
creer_utilisateur('charles', email='charles@gmail.com', role='user')
print('---')
creer_utilisateur('charles', email='charles@gmail.com', age=28, role='user')


print('\n'+'='*20)
print('Exercice 5')
print('='*20)
'''
## Exercice 5

Réponds avec tes propres mots :

1. Que contient `*args` ? 
    # les arguments positionneles
2. Quel type de donnée Python est créé ?
    # un tuple
3. Que contient `**kwargs` ?
    # des arguments nommés
4. Quel type de donnée Python est créé ?
    # un dictionnaire
5. Quand utiliserais-tu `*args` ou `**kwargs` ?'''
    # J'utiliserais *args lorsqu'une fonction doit accepter un nombre variable d'arguments positionnels et **kwargs lorsqu'elle doit accepter un nombre variable d'arguments nommés.