import re


def display_menu():
    print("""
=== Text Analyzer ===

1. Analyze text
2. Show statistics
3. Show top words
4. Search word
5. Show analysis history
0. Exit
""")


def get_choice(valid_choice = None):
    choice = input("Choice: ").strip()

    if valid_choice is None:
        valid_choice = ['0', '1', '2', '3', '4', '5']

    if choice in valid_choice:
        return choice

    return None


def get_filename():
    filename = input("Enter file name: ").strip()

    if filename:
        return filename

    return None


def cleanup_text(text):
    return