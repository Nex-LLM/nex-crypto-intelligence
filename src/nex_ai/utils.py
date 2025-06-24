"""
Collection of utility functions and helper classes.
This could include:
- Data formatting functions.
- Logging setup.
- Error handling decorators.
- Configuration loading.
"""

def format_timestamp(timestamp: int) -> str:
    """
    Formats a Unix timestamp into a human-readable string.
    """
    import datetime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def load_config(config_path: str) -> dict:
    """
    Loads configuration from a specified path (e.g., JSON, YAML).
    """
    print(f"Loading configuration from {config_path}...")
    return {"api_key": "dummy_key", "data_source": "mock"}
