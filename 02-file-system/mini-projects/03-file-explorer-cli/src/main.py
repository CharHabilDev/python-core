from pathlib import Path
from src.utils import display_menu, get_choice, get_extension
from src.explorer import (
    create_workspace, create_content, 
    list_files, list_directories,
    show_file_infos, search_by_extension,
    write_into_some_file
)


def main():
    workspace = create_workspace()
    root = Path(workspace.name)
    create_content(root)
    write_into_some_file(root)
    print(f"Workspace created: {root}")

    try:
        while True:
            display_menu()

            choice = get_choice()

            if choice is None:
                print("Invalid choice.")
                continue

            if choice == '1':
                list_files(root)

            elif choice == '2':
                list_directories(root)

            elif choice == '3':
                list_files(root)

                print()
                choice_file = get_choice()
                if choice_file is None:
                    print("Invalid choice.")
                    continue
                
                show_file_infos(choice_file, root)
            
            elif choice == '4':
                extension = get_extension()
                if extension is None:
                    print("Invalid extension.")
                    continue

                search_by_extension(extension, root) 

            else:
                break

    finally:
        workspace.cleanup()
        print("See you soon !")
        

if __name__ == '__main__':
    main()