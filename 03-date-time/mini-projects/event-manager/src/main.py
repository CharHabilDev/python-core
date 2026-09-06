from src.utils import (
    display_menu,
    get_user_choice
)

from src.events import (
    get_event_name,
    get_event_date,
    add_event,
    view_events,
    upcoming_events,
    get_event_id,
    delete_event
)

events = [
    {"name": "Event D", "date": "10/12/2027"},
    {"name": "Event A", "date": "05/10/2026"},
    {"name": "Event C", "date": "01/07/2027"},
    {"name": "Event B", "date": "25/12/2026"}
]


def main():
    while True:
        display_menu()

        choice = get_user_choice()

        if choice is None:
            print("Invalid choice.")
            continue

        if choice == '1':
            event_name = get_event_name()
            
            if event_name is None:
                print("Name cannot be empty.")
                continue

            event_date = get_event_date()
            if event_date is None:
                continue

            add_event(events, event_name, event_date)
            print("Event added successfully.")

        elif choice == '2':
            view_events(events)

        elif choice == '3':
            upcoming_events(events)

        elif choice == '4':
            event_id = get_event_id(events)
            if event_id is None:
                continue

            delete_event(events, event_id)
            print("Event deleted.")

        else:
            print("\nSee you soon!")
            break


if __name__ == '__main__':
    main()