from pathlib import Path

ALLOWED_EXTENSIONS = {".txt", ".pdf", ".png", ".jpg", ".py"}


def display_menu():
    print("""\nFile Explorer CLI

1. List files
2. List directories
3. Show file information
4. Search by extension
5. Exit\n""")


def get_choice(valid_choice = ['1', '2', '3', '4', '5']):
    choice = input("Choice : ").strip()

    if choice in valid_choice:
        return choice
    return None


def get_extension():
    print(f"\nAllowed extension : {ALLOWED_EXTENSIONS}")
    extension = input("\nEnter extension : ").strip()

    if extension in ALLOWED_EXTENSIONS or "."+extension in ALLOWED_EXTENSIONS:
        return extension if extension.startswith('.') else '.'+extension

    return None


def get_files(root: Path):
    return [file for file in root.rglob("*") if file.is_file()]