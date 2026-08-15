from validators import (
    validate_name, 
    validate_age,
    validate_email,
    validate_password
)


def get_user_choice():
    choice = input("Choix : ").strip()
    if choice in ['1', '2', '3', '4', '5']:
        return choice

    return None


def main():
    while True:
        print("\n1. Tester un nom")
        print("2. Tester un âge")
        print("3. Tester un email")
        print("4. Tester un mot de passe")
        print("5. Quitter\n")

        choice = get_user_choice()

        if choice is None:
            print("Choix invalide.")
            continue
        
        if choice == '5':
                break

        if choice == '1':
            name = input("Name : ").strip()

            try:
                validate_name(name)
                print("✓ Nom valide")
            except ValueError as err:
                print(f"✗ Erreur : {err}")

        elif choice == '2':
            age = input('Âge : ').strip()

            try:
                validate_age(age)
                print("✓ Âge valide")
            except (ValueError, TypeError) as err:
                print(f"✗ Erreur : {err}")

        elif choice == '3':
            email = input('Email : ').strip()

            try:
                validate_email(email)
                print("✓ Email valide")
            except ValueError as err:
                print(f"✗ Erreur : {err}")

        
        elif choice == '4':
            password = input('Mot de passe : ').strip()

            try:
                validate_password(password)
                print("✓ Mot de passe valide")
            except (ValueError, TypeError) as err:
                print(f"✗ Erreur : {err}")


if __name__ == '__main__':
    main()