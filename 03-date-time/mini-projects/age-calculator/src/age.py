from datetime import datetime, date


def get_user_birthdate():
    str_birthdate = input("Enter your birthdate (dd/mm/yyyy): ").strip()
    try:
        birthdate = datetime.strptime(str_birthdate, '%d/%m/%Y')
        if birthdate > datetime.now():
            print("Birthdate cannot be in the future.")
            return None
        return birthdate
    
    except ValueError:
        print("Error: invalid birthdate.")
        return None


def calculate_age(birthdate: datetime):
    today = datetime.today()
    birthday_passed = (
        (today.month, today.day) >=
        (birthdate.month, birthdate.day)
    )
    
    age = today.year - birthdate.year

    if not birthday_passed:
        age -=1
        
    return age


def calculate_days_lived(birthdate: datetime):
    return (datetime.now() - birthdate).days


def calculate_next_birthday(birthdate: datetime):
    today = date.today()

    current_year_birthday = date(
        year=today.year,
        month=birthdate.month,
        day=birthdate.day
    )

    if current_year_birthday < today:
        next_birthday = date(
            year=today.year + 1,
            month=birthdate.month,
            day=birthdate.day
        )
    else:
        next_birthday = current_year_birthday

    return next_birthday