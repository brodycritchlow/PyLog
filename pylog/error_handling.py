import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    print(f"Uncaught exception: {exc_type.__name__}: {exc_value}")

sys.excepthook = handle_exception

