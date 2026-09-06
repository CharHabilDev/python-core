from datetime import datetime

from src.utils import (
    display_menu,
    get_choice,
    display_remaining_time
)

from src.countdown import (
    get_event_date,
    calculate_remaining_time
)


def main():
    while True:
        display_menu()

        choice = get_choice()

        if choice is None:
            print("Invalid choice.")
            continue

        if choice in ["1", "2"]:
            event_date = get_event_date()

            if event_date is None:
                continue

        if choice == "1":

            if event_date.date() == datetime.today().date():
                print("Event is today.")
                continue

            remaining_time = calculate_remaining_time(event_date)

            print(
                f"Event in {remaining_time.days} days."
            )

        elif choice == "2":

            if event_date.date() == datetime.today().date():
                print(
                    f"\nEvent date : "
                    f"{event_date.strftime('%d/%m/%Y')}"
                )
                print("Remaining : today")
                continue

            remaining_time = calculate_remaining_time(event_date)

            print()

            display_remaining_time(
                remaining_time,
                event_date
            )

        else:
            print("\nSee you soon!")
            break


if __name__ == "__main__":
    main()