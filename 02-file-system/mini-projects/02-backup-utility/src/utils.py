def display_menu():
    print('\nBackup Utility\n')
    print('1. Backup file')
    print('2. Backup directory')
    print('3. List backups')
    print('4. Exit\n')


def get_choice(args='Choice : ', valid_choice=['1', '2', '3', '4']):
    choice = input(args).strip()
    if choice in valid_choice:
        return choice
    return None