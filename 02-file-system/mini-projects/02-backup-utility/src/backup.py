import tempfile
from pathlib import Path
import shutil


def create_workspace():
    return tempfile.TemporaryDirectory(prefix='sandbox_')


def create_workspace_content(root: Path):
    files = [
        'documents/notes.txt',
        'documents/todo.md', 
        'project/main.py', 
        'project/config.json'
    ]

    for file in files:
        (root/file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        (root/file).touch(exist_ok=True)


def list_available(choice:str, root:Path):
    if choice == '1':
        print('\nAvailable files:\n')
    else:
        print('\nAvailable directories:\n')
    
    i = 0
    for content in root.rglob("*"):
        if "backup" in content.parts:
            continue

        relative = content.relative_to(root)

        condition = content.is_file() if choice == '1' else content.is_dir() 
        
        if condition:
            i+=1
            print(f"{i}. {relative}")
    print('')


def backup_file(choice:str, root:Path):
    files = [
        root/'documents/todo.md',
        root/'documents/notes.txt',
        root/'project/main.py',
        root/'project/config.json'
    ]

    path = files[int(choice) - 1]

    destination_dir = root/'backup'

    destination_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    destination = destination_dir / path.name
    shutil.copy2(path, destination)


def backup_directory(choice:str, root:Path):
    directories = [
        root/'documents',
        root/'project'
    ]

    path = directories[int(choice) - 1]

    destination_dir = root/'backup'
    destination_dir.mkdir(
            parents=True,
            exist_ok=True
        )
    
    destination = destination_dir / path.name
    shutil.copytree(
        path, 
        destination,
        dirs_exist_ok=True       
    )


def list_backups(root:Path):
    backup = root/"backup"

    if backup.exists():
        elements = list(backup.iterdir())

        print(f"\nBackups content ({len(elements)} items):\n")

        for element in elements:
            print(element.name)

    else:
        print("No backup yet.")
