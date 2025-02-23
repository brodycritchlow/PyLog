import glob
import pylog.logger as lg
import pylog.error_handling
import sys

__all__ = []
for f in glob.glob('*.py'):
    if f != '__init__.py':
        file_name = f.split('/')[-1]
        file_name_without_extension = file_name.split('.')[0]
        __all__.append(file_name_without_extension)

logger = lg.Logger()
# sys.exceptionhook = pylog.error_handling.handle_exception