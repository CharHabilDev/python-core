from pathlib import Path

ALLOWED_EXTENSIONS = {".txt", ".md", ".doc", ".docx", ".py"}

def display_menu():
    print("\nTemporary Workspace Manager")
    print('\n1. Create file')
    print('2. List files')
    print('3. Exit\n')


def get_choice(valid_choice = ['1', '2', '3']):
    choice = input('Choice : ').strip()
    if choice in valid_choice:
        return choice
    return None


def get_file_name():
    print(f"Accepted file type : {ALLOWED_EXTENSIONS}")

    file_name = input("File name : ").strip()

    if not file_name:
        raise ValueError('Error: The file name cannot be empty.')

    file_name = Path(file_name)
    extension = file_name.suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Error: Invalid file type.")

    return file_name.stem+file_name.suffix.lower()