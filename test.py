from pylog import logger
import sys

logger.debug("Hello World!") 
logger.change(output=sys.stdout, format="[{level}] <==> {message} ({timestamp})")
logger.critical("Hello World 2")