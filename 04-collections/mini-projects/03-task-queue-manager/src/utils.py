from src.storage import load_data
from collections import namedtuple


Task = namedtuple(
    "Task",
    ['id', 'title', 'priority', 'status']
)


def display_menu() -> None:
    print("""
=== Task Manager ===

1. Add task
2. View pending tasks
3. Process next task
4. View completed tasks
5. Group tasks by priority
6. Show statistics
7. View recent actions
0. Exit
""")


def get_choice(valid_choice=None) -> str | None:
    choice = input("Choice: ").strip()

    if valid_choice is None:
        valid_choice = ['0', '1', '2', '3', '4', '5', '6', '7']

    if choice in valid_choice:
        return choice

    return None


def generate_id(data: list[dict], prefix: str) -> str:
    if not data:
        return f'{prefix}001'

    numbers = []
    for item in data:
        number_str = item['id'].replace(prefix, '')
        numbers.append(int(number_str))

    next_number = max(numbers) + 1
    return f"{prefix}{next_number:03d}"


def get_title() -> str:
    print()
    while True:
        title = input("Enter task title: ").strip()

        if title:
            return title.title()   


def get_priority(priorities: set | None = None) -> str | None:
    if priorities is None:
        priorities = {'Low', 'Medium', 'High'}
    
    while True:
        priority = input(f"Priority {priorities}: ").strip().capitalize()

        if priority in priorities:
            return priority
        

def create_task(
    task_id: str,
    title: str,
    priority: str,
    status: str
) -> Task:

    return Task(
        task_id,
        title,
        priority,
        status
    )


def convertion(data:list[dict]) -> list[Task]:
    new_data:list[Task] = []

    for item in data:
        user_item = Task(**item)
        new_data.append(user_item)

    return new_data