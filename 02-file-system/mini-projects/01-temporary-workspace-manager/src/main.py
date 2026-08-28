from pathlib import Path
from src.utils import display_menu, get_choice, get_file_name
from src.workspace import create_workspace, create_temp_file, list_workspace

def main():
    workspace = create_workspace()
    print("Workspace created: ")
    print(workspace.name)

    workspace_path = Path(workspace.name)

    try:
        while True:
            display_menu()

            choice = get_choice()

            if choice is None:
                print('Incorrect choice')
                continue

            elif choice == '1':

                try:
                    file_name = get_file_name()
                except ValueError as error:
                    print(error)
                    continue

                create_temp_file(workspace_path, file_name)

            elif choice == '2':
                print("\nFiles: ")    
                list_workspace(workspace_path)
            
            else:
                break
    finally:
        workspace.cleanup()
        print("See you soon !")

if __name__ == '__main__':
    main()