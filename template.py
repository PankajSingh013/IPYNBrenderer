import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
    )

while True:
    project_name = input("Input the project name:")
    if project_name !='':
        break

logging.info(f'Creating project by name: {project_name}')

#list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/_init__.py",
    f"tests/unit/_init__.py",
    f"tests/integration/_init__.py",
    "init_setup.sh",
    "requirments.txt"
    "requirments_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini", #to test our package in various environments
]

for filepath in list_of_files:
    filedir, filename = os.path.split(Path(filepath))
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directort at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        #will create an empty file based on filepath
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating a new file:{filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at {filepath}")

                         