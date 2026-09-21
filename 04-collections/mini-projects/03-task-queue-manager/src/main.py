from src.utils import (
    display_menu,
    get_choice
)

from src.tasks import (
    add_task,
    view_tasks,
    process_next_task,
    group_tasks,
    show_statistics,
    view_recent_actions
)


def main() -> None:
    while True:
        display_menu()

        choice = get_choice()

        if choice is None:
            print("Invalid choice.")
            continue

        if choice == '1':
            add_task()

        elif choice == '2':
            view_tasks(status='Pending')

        elif choice == '3':
            process_next_task()

        elif choice == '4':
            view_tasks(status='Completed')

        elif choice == '5':
            group_tasks()

        elif choice == '6':
            show_statistics()

        elif choice == '7':
            view_recent_actions()

        else:
            print("See you soon!")
            break


if __name__ == '__main__':
    main()