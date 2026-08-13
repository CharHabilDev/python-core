# Exercices

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

---

## Exercice 2

Crée une lambda qui additionne deux nombres.

Teste :

```python
addition(10, 5)
```

---

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

---

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

---

## Exercice 5

Réponds avec tes propres mots :

1. Qu'est-ce qu'une fonction lambda ?
2. Quelle différence principale existe entre une fonction classique et une lambda ?
3. Dans quels cas utiliserais-tu une lambda ?
4. Pourquoi évite-t-on les lambdas pour des traitements complexes ?