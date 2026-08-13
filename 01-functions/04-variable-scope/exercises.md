# Exercices

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

---

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

---

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

---

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

---

## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une variable locale ?
2. Qu'est-ce qu'une variable globale ?
3. Pourquoi faut-il limiter l'utilisation de `global` ?
4. Pourquoi les paramètres sont-ils considérés comme des variables locales ?
