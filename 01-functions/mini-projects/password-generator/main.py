from generator import generate_password


def main():
    print("Générateur de mots de passe : ")
    length = input("Longueur : ")
    uppercase = input("Majuscules ? (o/n) : ").strip().lower() == 'o'
    digits = input("Chiffres ? (o/n) : ").strip().lower() == 'o'
    symbols = input("Symboles ? (o/n) : ").strip().lower() == 'o'

    try:
        password = generate_password(
            int(length),
            uppercase,
            digits,
            symbols
        )

        print("Mot de passe généré :")
        print(password)
    except (ValueError, TypeError) as error:
        print(error)


if __name__ == "__main__":
    main()