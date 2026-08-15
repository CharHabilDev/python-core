import secrets
import string


def generate_password(
    length=12,
    uppercase=True,
    digits=True,
    symbols=False
):

    if not isinstance(length, int):
        raise TypeError("Erreur: l'argument 'length' doit être un entier (int).")

    if not isinstance(uppercase, bool) or not isinstance(digits, bool) or not isinstance(symbols, bool):
        raise TypeError("Erreur: les options doivent être des booléens (True/False)")

    if length <= 0:
        raise ValueError("Erreur: la longueur doit être suppérieur à 0.")
    
    characters = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )


if __name__ == "__main__":
    print(generate_password(14))
    print(generate_password())

    print(generate_password(20))

    print(generate_password(
                length=16,
                symbols=True
            ))

    try:
        print(generate_password(
            length=16,
            symbols=None
        ))
    except TypeError as error:
        print(error)