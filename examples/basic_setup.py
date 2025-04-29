import sys
from pylog import logger

# Configure the logger with a basic setup
logger.change(
    output=sys.stdout,  # Log output to the console
    level=Levels.INFO,  # Set the logging level to INFO
    format="<green>{timestamp}<reset> - <blue>{level}<reset>: {message}"  # Define a log format with colors
)

# Log messages at different levels
logger.debug("This is a DEBUG message.")  # This won't appear because the level is set to INFO
logger.info("This is an INFO message.")  # This will appear
logger.warning("This is a WARNING message.")  # This will appear
logger.error("This is an ERROR message.")  # This will appear
logger.critical("This is a CRITICAL message.")  # This will appear
