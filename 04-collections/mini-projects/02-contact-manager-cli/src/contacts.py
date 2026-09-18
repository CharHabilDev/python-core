from collections import (
    defaultdict, 
    Counter, 
    deque
)

from src.utils import (
    create_id, 
    get_name, 
    get_phone, 
    get_email, 
    get_city, 
    create_contact, 
    convertion
)

from src.storage import (
    load_data, 
    save_data
)


def load_data_file(filename: str) -> list | None:
    try:
        contacts = load_data(filename)
        return contacts
    
    except ValueError as error:
        print(error)
        return None


def convert_contact(filename: str):
    list_contacts:list[dict] = load_data_file(filename)
        
    if list_contacts is None:
        return None
        
    if not list_contacts:
        print("No contact yet!")
        return None

    return convertion(list_contacts)


def add_contact(filename='contacts.json') -> None:
    contacts = load_data_file(filename)

    if contacts is None:
        return

    contact_id = create_id(contacts, 'N')
    contact_name = get_name()
    contact_phone = get_phone()
    contact_email = get_email()
    contact_city = get_city()

    contact = create_contact(
        contact_id,
        contact_name,
        contact_phone,
        contact_email,
        contact_city
    )

    contacts.append(contact._asdict())

    save_data(filename, contacts) 
    print("Contact added successfully.")


def view_all_contacts(filename: str='contacts.json') -> None:
    contacts = convert_contact(filename)

    if contacts is None:
        return

    header = f"| {'ID':^4} | {'Name':^20} | {'Phone':^20} | {'Email':^30} | {'City':^20} |"

    print(f"\n{'======== ALL CONTACTS ========':^110}\n")

    print('-' * len(header))
    print(header)
    print('-' * len(header))
    
    for contact in contacts:
        print(
            f"| {contact.id:<4} | "
            f"{contact.name:<20} | "
            f"{contact.phone:<20} | "
            f"{contact.email:<30} | "
            f"{contact.city:<20} |"
        )
    print('-' * len(header))


def search_contact(contact_id:str, filename: str='contacts.json') -> None:
    contacts = convert_contact(filename)

    if contacts is None:
        return

    history = load_data_file('history.json')

    if history is None:
        history = []
    
    history = deque(history, maxlen=5)

    for contact in contacts:
        if contact.id == contact_id:

            history.append(contact.name)
            save_data('history.json', list(history))
            
            return (
                f"\n{'ID':<5}: {contact.id}\n"
                f"{'Name':<5}: {contact.name}\n"
                f"{'Phone':<5}: {contact.phone}\n"
                f"{'Email':<5}: {contact.email}\n"
                f"{'City':<5}: {contact.city}"
            )


def group_contact_by_city(filename: str = 'contacts.json') -> None:
    contacts = convert_contact(filename)

    if contacts is None:
        return

    groups_contacts = defaultdict(list)

    for contact in contacts:
        groups_contacts[contact.city].append(contact.name)

    sorted_contacts = sorted(groups_contacts.items(), key=lambda contact: contact[0])

    print("\n=== CONTACTS BY CITY ===")

    for contact in sorted_contacts:
        city, list_name = contact
        print(f"\n{city} ({len(list_name)})")
        print('-------------------------')

        for name in sorted(list_name):
            print(f"{name}")


def show_statistics(filename:str = 'contacts.json'):
    contacts = convert_contact(filename)

    if contacts is None:
        return

    city = [contact.city for contact in contacts]
    counter = Counter(city)

    total_contacts = sum(counter.values())

    print(f"\n=== CONTACT STATISTICS ===\n")
    print(
        f"{'Total contacts':<20}: {total_contacts}\n"
        f"{'Unique cities':<20}: {len(counter)}"
    )

    print(f"\nContacts by city\n")

    for key, val in counter.items():
        print(f"{f'{key}':<20}: {val}")

    print(f"\nMost represented city : {counter.most_common(1)[0][0]} ({counter.most_common(1)[0][1]} contacts)")
    

def show_recent_searches(filename: str = 'history.json'):
    history = load_data_file(filename)

    if history is None:
        return

    if not history:
        print("No recent searches yet!")
        return

    print("\n=== RECENT SEARCHES ===\n")

    for index, element in enumerate(history, start=1):
        print(f"{index}. {element}")