import json
import os
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from ensure import ensure_annotations

from src.winequalitymlops import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded from {path_to_yaml}")
            return ConfigBox(content)
    except Exception as e:
        raise ValueError(
            f"An error occurred while reading the YAML file at {path_to_yaml}: {e}"
        )


@ensure_annotations
def create__directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {directory}")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves data to a JSON file.

    Args:
        path (Path): The path where the JSON file will be saved.
        data (dict): The data to be saved in JSON format.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Data saved to JSON file at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The content of the JSON file as a ConfigBox object.
    """
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded from {path}")
    return ConfigBox(content) if isinstance(content, dict) else content


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path where the binary file will be saved.
    """
    joblib.dump(data, path)
    logger.info(f"Data saved to binary file at {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The content of the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data
