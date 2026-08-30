from pathlib import Path
from src.utils import display_menu, get_choice
from src.backup import (
    create_workspace, create_workspace_content,
    list_available, backup_file, 
    backup_directory, list_backups
)


def main():
    workspace = create_workspace()
    root = Path(workspace.name)
    create_workspace_content(root)
    print(f"Workspace created: {root}")

    try:
        while True:
            display_menu()

            choice = get_choice()
            if choice is None:
                print("Invalid choice.")
                continue

            if choice == '1':
                list_available('1', root)
                backup_choice = get_choice(args="Backup choice : ")
                
                if backup_choice is None:
                    print("Invalid choice.")
                    continue

                backup_file(backup_choice, root)
                print("\nFile backup successful.")


            elif choice == '2':
                list_available('2', root)
                backup_choice = get_choice(args="Backup choice : ", valid_choice=['1', '2'])
                                        
                if backup_choice is None:
                    print("Invalid choice.")
                    continue

                backup_directory(backup_choice, root)
                print("\nDirectory backup successful.")
            
            elif choice == '3':
                list_backups(root)

            else:
                break

    finally:
        print("\nCleaning sandbox...")
        workspace.cleanup()
        print("See you soon!")


if __name__ == '__main__':
    main()