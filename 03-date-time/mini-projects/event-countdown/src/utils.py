from datetime import datetime, timedelta


def display_menu():
    print("""
=== Event Countdown ===

1. Days Remaining
2. Detailed Countdown
0. Exit
""")


def get_choice(valid_choice=None):
    choice = input("Choice: ").strip()

    if valid_choice is None:
        valid_choice = ["0", "1", "2"]

    if choice in valid_choice:
        return choice

    return None


def display_remaining_time(
    remaining_time: timedelta,
    event_date: datetime
):
    time = timedelta(seconds=remaining_time.seconds)

    hours, minutes, seconds = str(time).split(":")

    print(f"Event date : {event_date.strftime('%d/%m/%Y')}")
    print(
        f"Remaining : "
        f"{remaining_time.days} days, "
        f"{hours} hours, "
        f"{minutes} minutes, "
        f"{seconds} seconds."
    )