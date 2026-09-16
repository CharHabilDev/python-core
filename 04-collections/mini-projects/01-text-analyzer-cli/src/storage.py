from pathlib import Path
import json

DEFAULT_DATA = []


def load_file(filename: str | Path) -> str | None:
    
    path = Path('data') / filename

    if not path.exists():
        return None

    with open(path, encoding='UTF-8') as file:
        return file.read()


def ensure_data_file(filename: str | Path) -> None:

    path = Path('data') / filename

    if not path.parent.exists():
        path.parent.mkdir(parents= True, exist_ok= True)
        
    if not path.exists():
        try:
            with path.open("w", encoding = 'utf-8') as file:
                json.dump(DEFAULT_DATA, file, indent=4, ensure_ascii=False)
        
        except PermissionError:
            print("Permission Denied")

        except OSError as error:
            print(f'System error : {error}')


def load_data(filename: str | Path) -> list:
    
    ensure_data_file(filename)

    path = Path('data') / filename

    try:
        with path.open("r", encoding='utf-8') as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        raise ValueError("Corrupted or invalid json file.")

    except PermissionError:
        raise ValueError("Permission denied while accessing rabbit data.")

    except OSError as error:
        raise ValueError(f'Unable to access rabbit data file: {error}')
    

def save_data(filename: str | Path , data: list) -> None:

    ensure_data_file(filename)

    path = Path('data') / filename

    try:
        with path.open("w", encoding='utf-8') as file:
            json.dump(
                data, 
                file, 
                indent=4, 
                ensure_ascii=False
            )
    
    except TypeError:
        print("Data not serializable in JSON.")

    except PermissionError:
        print("Permission Denied.")

    except OSError as error:
        print(f'System error : {error}.')