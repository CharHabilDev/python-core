'''
# Exercices

### Exercice 1

Crée une fonction `afficher_produit()` qui reçoit :

- nom
- prix

Puis appelle-la avec des arguments positionnels.
'''

def afficher_produit(nom, prix):
    print(f"{nom}: {prix} €")

afficher_produit('Clavier', 25)


'''
### Exercice 2

Appelle la même fonction avec des arguments nommés.
'''

afficher_produit(nom='Sac', prix=30)

'''
### Exercice 3

Crée une fonction `creer_utilisateur()` qui reçoit :

- username
- email
- age

Appelle-la :

1. avec uniquement des arguments positionnels ;
2. avec uniquement des arguments nommés ;
3. en mélangeant les deux.
'''
def creer_utilisateur(username, email, age):
    print(f'Username : {username} | Email: {email} | Âge: {age}')

# Appelle-la :

# 1. avec uniquement des arguments positionnels ;
creer_utilisateur('charles', 'charles@email.com', 27)

# 2. avec uniquement des arguments nommés ;
creer_utilisateur(
    username='charles',
    email='charles@email.com',
    age=27
)

# 3. en mélangeant les deux.
creer_utilisateur('charles', 'charles@email.com', age=27)


### Exercice 4

# 1. Quelle est la différence entre un paramètre et un argument ?
print(f"Un paramètre est une variable définie dans la signature d'une fonction.")
print(f"Un argument est la valeur qui est donné au paramètre d'une fonction")
# 2. Quelle est la différence entre un argument positionnel et un argument nommé ?
print(f"Un argument positionnel est transmis à une fonction selon sa position alors qu'un argument nommé est associo au paramètre cible.")
# 3. Dans quels cas préférerais-tu utiliser des arguments nommés ?
print("Lorsqu'une fonction prend beaucoup d'arguments. Cela rend le code plus lisible")
print("Les arguments nommés réduisent aussi les erreurs lorsqu'on ne se souvient plus de l'ordre des paramètres.")