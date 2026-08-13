def get_user_choice():
    choice = input("Choix : ").strip()
    if choice in ['1', '2', '3', '4', '5']:
        return choice

    return None


def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError('Error: Division par zéro')
        
    return a / b

def get_number():
    while True:
        try:
            return float(input('Entrer un nombre : '))
        except ValueError:
            print("Erreur : tu dois entrer un nombre valide.")


def main():
    while True:
        print('\n1. Addition')
        print('2. Soustraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Quitter\n')

        user_choice = get_user_choice()

        if user_choice is None:
            print("Choix invalide.")
            continue

        if user_choice == '5':
            break

        a = get_number()
        b = get_number()

        if user_choice == '1':
            resultat = addition(a, b)

        elif user_choice == '2':
            resultat = soustraction(a, b)

        elif user_choice == '3':
            resultat = multiplication(a, b)

        elif user_choice == '4':
            try:
                resultat = division(a, b)
            except ZeroDivisionError as error:
                print(error)
                continue

        print(f"Résultat : {resultat:.2f}")

if __name__ == '__main__':
    main()