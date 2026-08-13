'''
## Exercice 1

Crée une fonction :

```python
saluer()
```

Affiche :

```text
Bonjour
```

Puis :

```python
fonction = saluer
fonction()
```

Observe le résultat.
'''

def saluer():
    print("Bonjour")

fonction = saluer
fonction()



'''
## Exercice 2

Crée :

```python
def executer(fonction):
```

qui exécute la fonction reçue.

Teste avec :

```python
saluer()
```
'''

def executer(fonction):
    fonction()

executer(saluer)




'''
## Exercice 3

Crée :

```python
def creer_message():
```

qui retourne une fonction interne affichant :

```text
Bonjour
```

Teste le retour.
'''

def creer_message():
    def saluer():
        print("Bonjour")

    return saluer


function = creer_message()
function()


'''
## Exercice 4

Crée un décorateur :

```python
decorateur()
```

qui affiche :

```text
--- Début ---
```

avant l'exécution d'une fonction et :

```text
--- Fin ---
```

après.

Applique-le à :

```python
saluer()
```

avec la syntaxe :

```python
@decorateur
```
'''

def decorateur(func):

    def wrapper():
        print("--- Début ---")

        func()

        print("--- Fin ---")

    return wrapper


@decorateur
def saluer():
    print("Bonjour")

saluer()


'''
## Exercice 5

Réponds avec tes propres mots :

1. Pourquoi dit-on qu'une fonction est un objet en Python ?
    # parcequ'on peut : 
        - stocker une fonction dans une variable
        - passer une fonction comme argument
        - retourner une fonction depuis une autre
2. Que fait un décorateur ?
    # un décorateur prend une fonction en arguments en enrichit son comportement sans touché au code source de la fonction d'origine.
3. À quoi sert `wrapper()` ?
    # wrapper() est la fonction intermédiaire qui ajoute le nouveau comportement avant ou après l'exécution de la fonction originale.
4. À quoi correspond la syntaxe `@decorateur` ?
    # @decorateur est un raccourci pour écrire :
    # fonction = decorateur(fonction)
5. Dans quels frameworks ou bibliothèques as-tu déjà vu des décorateurs ?
    # Flask
    # FastAPI
    # pytest
'''