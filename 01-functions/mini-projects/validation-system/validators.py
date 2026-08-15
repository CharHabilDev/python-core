MIN_PASSWORD_LENGTH = 8
MAX_AGE = 120
MIN_NAME_LENGTH = 2


def validate_name(name):
    name = name.strip()
    if not name:
        raise ValueError("Le nom ne peut pas être vide.")

    if len(name) < MIN_NAME_LENGTH:
        raise ValueError("Le nom doit contienir au moins 2 caractères.")

    return name


def validate_age(user_age):
    try:
        age = int(user_age)
    except (ValueError, TypeError):
        raise ValueError("L'âge doit être un nombre entier valide.")

    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
        
    if age > MAX_AGE:
        raise ValueError("L'âge entré est trop élevé.")

    return age


def validate_email(email):
    if '@' not in email:
        raise ValueError("L'email doit contenir @.")
    if '.' not in email:
        raise ValueError("L'email doit contenir `.`.")

    return email


def validate_password(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"Le mot de passe doit contenir au moins {MIN_PASSWORD_LENGTH} caractères.")

    if not any(char.isalpha() for char in password):
        raise ValueError("Le mot de passe doit contenir au moins une lettre.")
    
    if not any(char.isdigit() for char in password):
        raise ValueError("Le mot de passe doit contenir au moins un chiffre.")

    return password

