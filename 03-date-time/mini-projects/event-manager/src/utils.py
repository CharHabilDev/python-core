from datetime import datetime


def display_menu():
    print("""
=== Event Manager ===

1. Add Event
2. View Events
3. Upcoming Events
4. Delete Event
0. Exit
""")


def get_user_choice(valid_choice=None):
    choice = input("Choice: ").strip()
    
    if valid_choice is None:
        valid_choice = ['0', '1', '2', '3', '4']

    if choice in valid_choice:
        return choice
    
    return None


def string_date_to_datetime(string_date: str):
    return datetime.strptime(string_date, '%d/%m/%Y')