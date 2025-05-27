import logging
import os
from pathlib import Path

project_name = "wine-quality-mlops"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]


def create_project_structure():
    """
    Create the project structure based on the predefined list of files.
    """
    for file_path in list_of_files:
        # Create directories if they do not exist
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Create the file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                pass  # Create an empty file
            logging.info(f"Created file: {file_path}")
        else:
            logging.warning(f"File already exists: {file_path}")


if __name__ == "__main__":
    create_project_structure()
