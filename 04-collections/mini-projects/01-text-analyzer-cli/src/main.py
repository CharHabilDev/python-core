from src.utils import (
    display_menu,
    get_choice,
    get_filename
)

from src.analyzer import (
    analyze_file
)

from src.menu import (
    show_statistics,
    show_top_words,
    display_search_result,
    display_analyses_history
)


def main():
    counter = None
    text = None

    while True:
        display_menu()

        choice = get_choice()
        if choice is None:
            print("Invalid choice.")
            continue

        if choice == '1':
            filename = get_filename()
            if filename is None:
                print("Invalid filename.")
                continue

            result =  analyze_file(filename)

            if result is not None:
                text, counter = analyze_file(filename)

        elif choice == '2':
            if counter is None:
                print("No analysis available.")
                continue

            show_statistics(counter, text)
            
        elif choice == '3':
            if counter is None:
                print("No analysis available.")
                continue

            n = input("Enter number of top words to display: ").strip()
            if not n:
                print("Number cannot be empty.")
                continue
            try:
                n = int(n)
            except ValueError:
                print("You must be enter the valid number.")
                continue

            show_top_words(counter, n)

        elif choice == '4':
            if counter is None:
                print("No analysis available.")
                continue

            word = input("Enter a word: ").strip()
            if not word:
                print("Word cannot be empty.")
                continue
                
            display_search_result(counter, word)

        elif choice == '5':
            display_analyses_history()

        else:
            print("See you soon!")
            break


if __name__ == '__main__':
    main()