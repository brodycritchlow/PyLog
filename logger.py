import typing
from _enums import Levels

class Logger:
    """A central hub for routing log messages to various handlers.

    The Logger is the backbone of PyLog, serving as the primary interface for all logging operations.
    Its simplicity and flexibility make it an ideal choice for managing log output in your application.

    With PyLog, you can start logging messages immediately after importing the module. The logger is
    pre-configured to output logs to the console by default, but you can easily add custom handlers
    using the change method. Logs can be formatted using a variety of severity levels and message templates.

    Each log message is accompanied by a rich set of contextual information, including timestamp,
    function name, file path, line number, and thread ID. This metadata provides valuable insights
    into your application's behavior and helps you diagnose issues more efficiently.

    To get started with PyLog, simply import the logger module and begin logging messages. There's no
    need to create a logger instance manually – PyLog takes care of the details for you.
    """
    
    def __init__(self):
        ...
        
    def change(self, output: typing.TextIO | typing.BinaryIO, *, level: Levels = Levels.INFO, format: str)
        ...