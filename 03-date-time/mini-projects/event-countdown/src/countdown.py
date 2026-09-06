from datetime import datetime


def get_event_date():
    str_event_date = input("Enter event date (dd/mm/yyyy): ").strip()

    try:
        event_date = datetime.strptime(str_event_date, "%d/%m/%Y")

        if event_date.date() < datetime.today().date():
            print("Error: event date cannot be in the past.")
            return None

        return event_date

    except ValueError:
        print("Error: invalid event date.")
        return None


def calculate_remaining_time(event_date: datetime):
    return event_date - datetime.now()