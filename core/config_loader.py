import json
import os

# Load from project config/settings.json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "settings.json")

DEFAULT_CONFIG = {
    "model": "gemini-2.0-flash",   # fallback model
    "api_key": "",
    "os": "windows",              # fallback OS
    "temperature": 0.4            # safe default for command generation
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config file missing: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)

    merged = DEFAULT_CONFIG.copy()
    merged.update({k: v for k, v in data.items() if v is not None})

    return merged


# ----------------------------------------------------
# NEW FUNCTION: update a config key in settings.json
# ----------------------------------------------------
def update_config(key: str, value):
    """Update a single config value and write back to settings.json."""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config file missing: {CONFIG_PATH}")

    # Load existing config
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    # Apply update
    config[key] = value

    # Save back to disk with pretty formatting
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    return True
