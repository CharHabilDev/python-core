from collections import deque, defaultdict, Counter

from src.storage import load_data, save_data

from src.utils import (
    generate_id,
    get_title,
    get_priority,
    create_task,
    convertion,
    Task
)


def load_file_data(filename: str) -> list[dict] | list | None:
    try:
        data = load_data(filename)
        return data
    
    except ValueError as err:
        print(err)
        return None


def convert_task(filename:str) -> list[Task]:
    list_task = load_file_data(filename)

    if list_task is None:
        return None

    if not list_task:
        print("No task yet!")
        return None

    return convertion(list_task)


def add_task(filename =  'tasks.json') -> None:
    tasks = load_file_data(filename)  

    if tasks is None:
        return
    
    task_id = generate_id(tasks, "T")
    task_title = get_title()
    task_priority = get_priority()

    task = create_task(
        task_id,
        task_title,
        task_priority,
        "Pending"
    )

    tasks.append(task._asdict())
    tasks = sorted(tasks, key=lambda task: task['id'])

    add_action(task_id, task_title, 'add')
    
    try:
        save_data(filename, tasks)
    except ValueError as err:
        print(err)
        return
    print("\nTask added successfully.")


def view_tasks(status: str, filename = 'tasks.json') -> None:
    tasks = convert_task(filename)

    if tasks is None:
        return
    
    status_tasks = [task for task in tasks if task.status == status.capitalize()]

    print(f"\n=== {status.upper()} TASKS ===\n")
    print(f"{f'ID':<6} | {f'PRIORITY':<10} | {f'TITLE'}")
    print("-----------------------------------------------------------")

    for task in status_tasks:
        print(
            f"{f"{task.id:<6}"} | "
            f"{f"{task.priority.upper():<10}"} | "
            f"{f"{task.title}"}"
        )


def process_next_task(filename = 'tasks.json') -> None:
    tasks = convert_task(filename)

    if tasks is None:
        return

    pending_tasks = [task for task in tasks if task.status == 'Pending']

    if not pending_tasks:
        print("No task pending.")
        return

    pending_tasks = deque(pending_tasks)
    
    pop_task = pending_tasks.popleft()

    for index, task in enumerate(tasks): 
        if task.id == pop_task.id:
            tasks[index] = task._replace(status='Completed')
            break

    add_action(pop_task.id, pop_task.title, 'process')
    save_data(filename, [t._asdict() for t in tasks])

    print(
        f"\n========================================\n"
        f"TASK COMPLETED : {pop_task.id}\n"
        f"========================================\n"
        f"Title    : {pop_task.title}\n"
        f"Priority : {pop_task.priority}\n"
        f"Status   : Completed\n"
        f"========================================\n"
    )


def group_tasks(filename = 'tasks.json') -> None:
    tasks = convert_task(filename)

    if tasks is None:
        return

    grouped = defaultdict(list)

    for task in tasks:
        grouped[task.priority].append(task.title)

    priority_order = ["High", "Medium", "Low"]

    for priority in priority_order:
        if priority not in grouped:
            continue

        titles = grouped[priority]

        print(f"\n{priority.upper()} ({len(titles)})")
        print("-------------------------")

        for title in sorted(titles):
            print(title)


def show_statistics(filename = 'tasks.json') -> None:
    tasks = convert_task(filename)

    if tasks is None:
        return

    status = [s.status for s in tasks]
    priority = [p.priority for p in tasks]

    counter_status = Counter(status)
    counter_priority = Counter(priority)

    print(f"\n=== TASK STATISTICS ===\n")
    
    print("By Status\n")

    status_order = ['Pending', 'Completed']

    for status in status_order:
        print(
                f"{status:<10}: "
                f"{counter_status.get(status, 0)}"
            )

    print("\nBy Priority\n")

    priority_order = ["High", "Medium", "Low"]

    for priority in priority_order:
        print(
            f"{priority:<10}: "
            f"{counter_priority.get(priority, 0)}"
        )


def view_recent_actions(filename = 'history.json') -> None:
    history = load_file_data(filename)

    if not history:
        print("No recent actions.")
        return

    print("Note: [+] = add | [✓] = completed")

    print("\n=== RECENT ACTIONS ===\n")
    for action in history:
        print(action)


def add_action(
    task_id: str,
    task_title: str,
    type: str,
    filename = 'history.json'
) -> None:
    history = load_file_data(filename)

    if history is None:
        history = []

    history = deque(history, maxlen=5)

    types = {'add': '[+]', 'process': '[✓]'}

    content = f"{types.get(type.lower(), '[ ]')} {task_id} - {task_title}"

    history.append(content)

    try:
        save_data(filename, list(history))
    except ValueError as err:
        print(err)