from src.utils import display_menu, get_choice
from src.age import get_user_birthdate, calculate_age, calculate_days_lived, calculate_next_birthday


def main():
    while True:
        display_menu()

        choice = get_choice()

        if choice is None:
            print("Invalid choice.")
            continue

        if choice in ["1", "2", "3"]:
            birthdate = get_user_birthdate()

            if birthdate is None:
                continue

        if choice == '1':        
            age = calculate_age(birthdate)
            print(f"You're {age} years old.")

        elif choice == '2':
            days = calculate_days_lived(birthdate)
            print(f"You have lived {days} days.")

        elif choice == '3':
            next_birthday = calculate_next_birthday(birthdate).strftime("%d/%m/%Y")
            print(f"Your next birthday is on {next_birthday}.")

        else:
            print("\nSee you soon !")
            break


if __name__ == '__main__':
    main()