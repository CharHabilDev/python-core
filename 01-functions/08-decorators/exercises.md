# Exercices

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

---

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

---

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

---

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

---

## Exercice 5

Réponds avec tes propres mots :

1. Pourquoi dit-on qu'une fonction est un objet en Python ?
2. Que fait un décorateur ?
3. À quoi sert `wrapper()` ?
4. À quoi correspond la syntaxe `@decorateur` ?
5. Dans quels frameworks ou bibliothèques as-tu déjà vu des décorateurs ?
