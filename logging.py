import sys
import json
from datetime import datetime
from _enums import Levels

_config = {
    "log_level": Levels.INFO,
    "log_to_file": None,
    "json_format": False
}

def setup(log_level="INFO", log_to_file=None, json_format=False):
    """Configures the custom logger."""
    if log_level.upper() not in Levels.__members__:
        raise ValueError(f"Invalid log level: {log_level}")

    _config["log_level"] = Levels[log_level.upper()]
    _config["log_to_file"] = log_to_file
    _config["json_format"] = json_format

def _should_log(level: Levels):
    """Checks if the log level is high enough to be logged."""
    return list(Levels).index(level) >= list(Levels).index(_config["log_level"])

def _format_log(level: Levels, message: str):
    """Formats the log message."""
    timestamp = datetime.utcnow().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "level": level.value,
        "message": message
    }
    
    return json.dumps(log_entry, ensure_ascii=False) if _config["json_format"] else f"{timestamp} - {level.value}: {message}"

def _write_log(message: str):
    """Writes the log message to the configured outputs."""
    print(message, file=sys.stdout)
    if _config["log_to_file"]:
        with open(_config["log_to_file"], "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")

def log(level: Levels, message: str):
    """Generic logging function."""
    if not isinstance(level, Levels):
        raise ValueError(f"Invalid log level: {level}")
    
    if _should_log(level):
        log_message = _format_log(level, message)
        _write_log(log_message)

def debug(message): log(Levels.DEBUG, message)
def info(message): log(Levels.INFO, message)
def warning(message): log(Levels.WARNING, message)
def error(message): log(Levels.ERROR, message)
def critical(message): log(Levels.CRITICAL, message)
