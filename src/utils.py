# utils.py

import os
import json
from datetime import datetime
import logging
from typing import Dict

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_current_datetime() -> datetime:
    """Returns the current datetime object."""
    return datetime.now()

def get_current_date() -> str:
    """Returns the current date as a string in 'YYYY-MM-DD' format."""
    return datetime.now().strftime('%Y-%m-%d')

def get_config() -> Dict:
    """Loads configuration from 'config.json' file."""
    with open('config.json') as f:
        return json.load(f)

def save_config(config: Dict) -> None:
    """Saves configuration to 'config.json' file."""
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def get_env_value(env_var: str) -> str:
    """Returns the value of the given environment variable."""
    return os.getenv(env_var)