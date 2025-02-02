import os
from box.exceptions import BoxValueError
import yaml
from machine_learning_project import MLLogger
import json
import joblib
from ensure import ensure_annotations
from box import Box
from typing import Any
from pathlib import Path

log= MLLogger('Ml_logger')

@ensure_annotations
def read_yaml(path_to_yaml_file:Path) -> Box:
    """
    Read YAML file and convert it to a Box object.

    Args:
    path_to_yaml_file (Path): Path to the YAML file.
    
    Returns:
    Box: A Box object containing the YAML file contents.
    """
    try:
        with open(path_to_yaml_file, 'r') as file:
            yaml_data = yaml.safe_load(file)
            log.info(f'yaml file:{path_to_yaml_file} loaded Succesfully')
            return Box(yaml_data)
    
    except BoxValueError:
        raise ValueError('Yaml is empty')
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_the_directories:Path, verbose= True):

    for path in path_to_the_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                log.info(f'Directory {path} created')
        except Exception as e:
            log.error(f'Error creating directory {path}: {e}')

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data to a file
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        log.info(f"json file saved at: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_json(path: Path) -> Box:
    """
    Load json files data
    
    Args:
        path (Path): path to json file

    Returns:
        Box: data as class attributes instead of dict
    """
    try:
        with open(path) as f:
            content = json.load(f)
        log.info(f"json file loaded successfully from: {path}")
        return Box(content)
    except Exception as e:
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=path)
        log.info(f"binary file saved at: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data
    
    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path)
        log.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        raise e

def get_size(path: Path) -> str:
    """
    Get size of file in KB
    
    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        raise e
if __name__ == '__main__':
    # Example usage
    yaml_path = Path('config/config.yaml')
    config = read_yaml(yaml_path)
    print(f"Yaml file: {yaml_path}")
    print(config)