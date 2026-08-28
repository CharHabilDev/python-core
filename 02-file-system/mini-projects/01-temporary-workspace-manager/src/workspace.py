import tempfile
from pathlib import Path


def create_workspace():
    return tempfile.TemporaryDirectory(prefix='workspace_')
    

def create_temp_file(workspace_path:Path, file_name:str):
    
    path = workspace_path / file_name

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    path.touch(exist_ok=True)

    print(f"\File '{file_name}' created.")


def list_workspace(workspace_path:Path):
    files = [file for file in workspace_path.rglob('*') if file.is_file()]

    print(f"\nNumber of files: {len(files)}")

    if not files:
        print("No files yet.")
        return

    for file in files:
        print(file.name)