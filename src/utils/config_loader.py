import yaml
from typing import Any

def load_config(config_path: str) -> Any:
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
