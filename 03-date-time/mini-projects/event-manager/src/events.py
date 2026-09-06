from datetime import datetime
from src.utils import string_date_to_datetime


def get_event_name():
    event_name = input("Event name: ").strip()

    if event_name:
        return event_name
    
    return None


def get_event_date():
    str_event_date = input("Event date (dd/mm/yyyy): ").strip()
    
    try:
        event_date = string_date_to_datetime(str_event_date)
        
        if event_date.date() < datetime.today().date():
            print("Error: event date cannot be in the past.")
            return None
        
        return event_date
    
    except ValueError:
        print("Error: invalid event date.")


def add_event(
    events: list[dict],
    event_name:str,
    event_date:datetime
):
    events.append(
        {
            'name': event_name,
            'date': event_date.date().strftime("%d/%m/%Y")
        }
    )


def view_events(events:list[dict]):
    if not events:
        print("No event yet.")
        return

    print("\n=== Events ===\n")
    events.sort(
        key=lambda event: 
        string_date_to_datetime(event['date'])
    )
    
    for index, event in enumerate(events, start=1):
        print(f"{index}. {event['name']} - {event['date']}")


def calculate_remaining_time(event_date:datetime):
    return event_date - datetime.today()


def upcoming_events(events:list[dict]):
    if not events:
        print("No event yet.")
        return

    print("\n=== Upcoming Events ===\n")
    events.sort(
            key=lambda event: 
            string_date_to_datetime(event['date'])
        )
    
    for event in events:
        print(event['name'])
        print(f"Date: {event['date']}")
        
        event_date = string_date_to_datetime(event['date'])
        
        if event_date.date() == datetime.today().date():
            remaining_time = 'today'
            print(f"Remaining: {remaining_time}\n")
        
        else:
            remaining_time = calculate_remaining_time(event_date)
            print(f"Remaining: {remaining_time.days} days\n")


def get_event_id(events:list[dict]):
    str_event_id = input("Event ID: ").strip()
    
    try:
        event_id = int(str_event_id)
        
        if event_id > len(events):
            print(f"Error: event ID cannot be greater than {len(events)}.")
            return None
        
        if event_id <= 0:
            print("Error: event ID must be greater than 0.")
            return None
        
        return event_id
    
    except ValueError:
        print("Error: invalid event ID.")
        return None


def delete_event(
    events:list[dict],
    event_id:int
):
    events.pop(event_id-1)