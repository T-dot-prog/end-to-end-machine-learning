import os
import pathlib
import logging

# Set up logging

logging.basicConfig(filename='file_operations.log', level=logging.INFO)

project_name= 'machine_learning_project'

# Create project directory
list_of_files= [
    ".github/workflow/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/entity_config.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'research/trails.ipynb',
    'setup.py',
    'templates/index.html',


]

for file_path in list_of_files:
    file_path = pathlib.Path(file_path)
    file_dir, file_name= os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f'Created directory: {file_dir}')

    if (not os.path.exists(file_path)) or os.path.getsize(file_path) ==0:
        with open(file_path, 'w') as file:
            pass
            logging.info(f'Created file: {file_path}')
    else:
        logging.info(f'File {file_path} already exists')
