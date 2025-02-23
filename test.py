from pylog import logger, error_handling
import pylogstyles
import sys

logger.change(output=open("TEST.txt", "w+"), format="<blue><underline>{level}<reset> - {message}")
logger.debug("Hello World!") 
logger.critical("Hello World 2")

raise KeyError("test")
