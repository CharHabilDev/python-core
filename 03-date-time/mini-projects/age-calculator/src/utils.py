def display_menu():
    print("""
=== Age Calculator ===

1. Calculate Age
2. Days Lived
3. Next Birthday
0. Exit
""")


def get_choice(valid_choice=None):
    choice = input("Choice: ").strip()

    if valid_choice is None:
        valid_choice = ['0', '1', '2', '3']
        
    if choice in valid_choice:
        return choice
    return None
    