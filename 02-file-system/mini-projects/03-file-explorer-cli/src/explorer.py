from pathlib import Path
import tempfile
from src.utils import get_files


FILES = [
        'documents/notes.txt',
        'documents/report.pdf',
        'images/logo.png',
        'images/photo.jpg',
        'scripts/main.py'
    ]


def create_workspace():
    return tempfile.TemporaryDirectory(prefix='workspace_')


def create_content(root:Path):
    for file in FILES:
        (root/file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        (root/file).touch(exist_ok=True)


def list_files(root:Path):
    files = get_files(root)
    print(f"\nWorkspace content ({len(files)} files) :\n") 

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")


def list_directories(root:Path):
    directories = [directory for directory in root.rglob('*') if directory.is_dir()]
    print(f"\nWorkspace content ({len(directories)} directories):\n")
   
    for index, directory in enumerate(directories, start=1):
        print(f"{index}. {directory.name}")


def show_file_infos(choice:str, root:Path):
    files = get_files(root)
    path = root/files[int(choice) - 1]

    print(f"\n{'Name':<10}: {path.name}")
    print(f"{'Extension':<10}: {path.suffix}")
    print(f"{'Size':<10}: {path.stat().st_size} bytes")
    print(f"{'Path':<10}: {path.relative_to(root)}")


def search_by_extension(extension:str, root:Path):
    files = [file for file in root.rglob(f'*{extension}')]

    if not files:
        print('No file found.')
        return

    print("\nFile(s) found.")
    for file in files:
        print(file.relative_to(root))


def write_into_some_file(root:Path):
    (root/FILES[0]).write_text("""Notes importantes :
- Penser à vérifier le fichier de configuration avant le déploiement.
- Sauvegarde automatique configurée via le script main.py.
""", 
encoding='utf-8')

    (root/FILES[1]).write_text("""Ce document PDF a été formaté et généré avec plusieurs dimensions de texte bien 
distinctes pour assurer une hiérarchie visuelle claire :
- Grand Titre Principal (taille 26 pt) : "Rapport d'Exécution du Projet".
- Sous-titres de Sections (taille 16 pt) : Structuration claire des parties.
- Corps de Texte (taille 11 pt) : Un texte rédigé abordant la synthèse globale de l'automatisation 
et l'analyse de l'intégrité des données système.
""", 
encoding='utf-8')

    (root/FILES[-1]).write_text("""def get_choice(valid_choice = ['1', '2', '3', '4', '5']):
    choice = input("Choice : ").strip()

    if choice in valid_choice:
        return choice
    return None""", 
    encoding='utf-8')
    