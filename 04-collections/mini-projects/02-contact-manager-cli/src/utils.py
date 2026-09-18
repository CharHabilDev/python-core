import re
from collections import namedtuple


Contact = namedtuple(
    "Contact",
    ["id", "name", "phone", "email", "city"]
)


def display_menu() -> None:
    print("""
=== Contact Manager ===

1. Add a contact
2. View all contacts
3. Search a contact
4. Group contacts by city
5. Show contact statistics
6. View recent searches
0. Exit
""")


def get_user_choice(valid_choice = None) -> None | str:
    choice = input("Choice: ").strip()

    if valid_choice is None:
        valid_choice = ['0', '1', '2', '3', '4', '5', '6']

    if choice in valid_choice:
        return choice

    return None


def create_id(data: list, prefix: str) -> str:
    #prefix: N
    if not data:
        return f'{prefix}001'

    number = []

    for item in data:
        number_str = item['id'].replace(prefix, '')
        number.append(int(number_str))

    next_number = max(number) + 1
    return f'{prefix}{next_number:03d}'


def get_name() -> str:
    while True:
        name = input("Name: ").strip()

        if name:
            return name.title()


def get_phone() -> str:
    while True:
        phone = input("Enter phone number (Ex: +2290144752517): ").strip()

        pattern = r"^\+[1-9]\d{6,14}$"
        
        if re.fullmatch(pattern, phone):
            return phone


def get_email() -> str:
    while True:
        email = input("Enter email address: ").strip()

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.fullmatch(pattern, email):
            return email
        

def get_city() -> str:
    while True:
        city = input("Enter contact city: ").strip()

        if city:
            return city.title()


def get_contact_id() -> str | None:
    contact_id = input("Enter contact ID: ").strip().upper()

    if contact_id.startswith('N') and len(contact_id) == 4 and contact_id[1:].isdigit():
        return contact_id
    
    return None


def create_contact(
    contact_id:str,
    name: str,
    phone: str,
    email: str,
    city: str
) -> Contact:

    return  Contact(
        contact_id,
        name,
        phone,
        email,
        city
    )


def convertion(contacts:list[dict]) -> list[Contact]:
    """Convert the list contact to namedtuple objet"""
    new_contacts: list[Contact] = []

    for contact in contacts:
        user_contact = Contact(**contact)
        new_contacts.append(user_contact)

    return new_contacts