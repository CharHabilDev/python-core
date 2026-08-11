'''
## Exercice 1

Crée une fonction `saluer()` qui possède :

- un paramètre `nom`
- une valeur par défaut `"Invité"`

Teste :

```python
saluer()
saluer("Ali")
```
'''

def saluer(nom='Invité'):
    print(f"Bonjour {nom}")

saluer()
saluer('Ali')


'''
## Exercice 2

Crée une fonction `afficher_produit()` avec :

- nom
- prix=0

Teste plusieurs appels.
'''

def afficher_produit(nom, prix=0):
    print(f"{nom}: {prix} €")

afficher_produit('Souris')
afficher_produit('SSD', 399.99)


'''
## Exercice 3

Crée une fonction `creer_utilisateur()` avec :

- username
- role="user"

Teste :

```python
creer_utilisateur("charles")
creer_utilisateur("charles", "admin")
```
'''

def creer_utilisateur(username, role='user'):
    print(f"Username: {username} | Rôle: {role}")

creer_utilisateur('charles')
creer_utilisateur('charles', 'admin')


'''
## Exercice 4

Crée une fonction `creer_evenement()` avec :

- titre
- lieu="Non défini"
- capacite=50

Teste :

```python
creer_evenement("Hackathon")
creer_evenement("Hackathon", "Cotonou")
creer_evenement("Hackathon", "Cotonou", 200)
```
'''

def creer_evenement(titre, lieu="Non défini", capacite=50):
     print(f'{titre} aura lieu à {lieu} dans une sale de {capacite} places.')

creer_evenement("Hackathon")
creer_evenement("Hackathon", "Cotonou")
creer_evenement("Hackathon", "Cotonou", 200)


'''

## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une valeur par défaut ?
    # Une valeur par défaut est une valeur automatiquement utilisée lorsqu'aucun argument n'est fourni pour ce paramètre.
2. Pourquoi utilise-t-on des valeurs par défaut ?
    # 
       - Simplifier les appels : évite d'écrire les arguments pour les cas les plus fréquent
       - Permet de personnaliser le comportement de la fonction si nécessaire
3. Pourquoi les paramètres avec valeurs par défaut doivent-ils être placés après les paramètres obligatoires ?
    # Pour éviter toute ambiguïté lors de l'appel de la fonction
'''
