# Exercises

## Exercise 1

What does `count()` return?

- `count()` return an iterator

---

## Exercise 2

Complete:

count()
↓
0
1
2
3
4
...
∞

---

## Exercise 3

Complete:

count(5)

↓
5
6
7
8
...

---

## Exercise 4

Complete:

count(0, 2)

↓
0
2
4
6
8
...

---

## Exercise 5

Complete:

count(10, -2)

↓
10
8
6
4
2
...

---

## Exercise 6

True or False?

- `count()` is infinite. `True`
- `count()` returns a list. `False`
- `count()` uses lazy evaluation. `True`
- `count()` can use negative steps. `True`

---

## Exercise 7

What is the difference between:

- `range()`
- `count()`

range() produit une séquence finie de nombres.
count() produit une séquence infinie de nombres.
range() possède une limite alors que count() continue indéfiniment.

---

## Exercise 8

Give three practical use cases for `count()`.

- Créer des identifiants (ID001, ID002...)
- Numéroter des éléments
- Simuler des tours dans un jeu ou une boucle


---

## Exercise 9

Why is `count()` memory efficient?

`count()` est économe en mémoire car il ne stocke pas toute la séquence.
Il conserve uniquement son état actuel et génère la valeur suivante lorsqu'elle est demandée.

---

## Exercise 10

Explain what happens when `next()` is called repeatedly on a `count()` iterator.

À chaque appel de `next()`, `count()` génère la valeur suivante selon la valeur de départ et le pas défini.
L'iterator avance d'un élément à chaque appel.