# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
import yaml
from pathlib import Path
from data_classes import Config

def load_config(config_file: str = "config.yaml") -> Config:
    """Loads the YAML configuration file and parses it using the Pydantic data classes."""

    with open(config_file, 'r') as file:
        config_dict = yaml.safe_load(file)

    config = Config(**config_dict)
    return config

if __name__ == "__main__":
    config = load_config()
    print("Data Path:", config.data.data_path)
    print("Model Parameters:", config.model.params)
