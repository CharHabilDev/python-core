### Exercice 1

Crée :

```python
Path("documents/notes.txt")
```

Affiche :

```text
name
stem
suffix
parent
```

---

### Exercice 2

Crée :

```python
Path("images/photo.jpg")
```

Affiche :

```python
.parts
```

---

### Exercice 3

Crée un objet représentant un fichier qui n'existe probablement pas :

```python
Path("fichier_inexistant.txt")
```

Affiche :

```python
.exists()
```

---

### Exercice 4

Teste sur un fichier réel de ton projet :

```python
.is_file()
```

---

### Exercice 5

Teste sur un dossier réel de ton projet :

```python
.is_dir()
```

---

### Exercice 6

Réponds avec tes propres mots :

1. Différence entre `.name` et `.stem` ?
2. Que retourne `.suffix` ?
3. Que retourne `.parent` ?
4. Que contient `.parts` ?
5. Différence entre `.exists()`, `.is_file()` et `.is_dir()` ?

Comme pour les chapitres précédents, fais d'abord les exercices. La correction viendra ensuite.
