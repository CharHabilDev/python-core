from src.utils import (
    display_menu, 
    get_user_choice, 
    get_contact_id
)

from src.contacts import (
    add_contact, 
    view_all_contacts, 
    search_contact, 
    group_contact_by_city, 
    show_statistics, 
    show_recent_searches
)


def main() -> None:
    while True:
        display_menu()

        choice = get_user_choice()

        if choice is None:
            print("Invalid choice.")
            continue

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_all_contacts()

        elif choice == '3':
            contact_id = get_contact_id()
            
            if contact_id is None:
                print("Invalid contact id.")
                continue

            contact = search_contact(contact_id)

            if contact is None:
                print("Contact no found!")
                continue

            print(contact)

        elif choice == '4':
            group_contact_by_city()

        elif choice == '5':
            show_statistics()

        elif choice == '6':
            show_recent_searches()

        else:
            print("See you soon!")
            break


if __name__ == '__main__':
    main()