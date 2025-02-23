import sys
import threading

def handle_exception(exc_type, exc_value, exc_traceback):
    import traceback
    from pylog import logger
    tb = traceback.extract_tb(exc_traceback)
    file, line, function = tb[-1][0], tb[-1][1], tb[-1][2]
    thread_id = threading.get_ident()
    if issubclass(exc_type, Exception):
        logger.error(message=str(exc_value), file=file, function=function, line=line, thread_id=thread_id, exception=exc_value)
    else:
        logger.critical(message=str(exc_value), file=file, function=function, line=line, thread_id=thread_id, exception=exc_value)

sys.excepthook = handle_exception
