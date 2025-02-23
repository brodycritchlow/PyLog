import typing
from pylog._enums import Levels
from datetime import datetime, date
from pathlib import Path
import sys
from pylogstyles import Colors, TextStyles

AcceptableRotations = typing.Union[str, int, date, typing.Callable[[datetime], bool]]
AcceptableOutput = typing.Union[typing.IO[typing.Any], str, Path, typing.Callable[[str], None], typing.Coroutine[typing.Any, typing.Any, typing.Any]]

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
    
    def __init__(self, output: AcceptableOutput = sys.stdout, level: Levels = Levels.INFO, format: str = "{level} - {message}", rotation: AcceptableRotations = ""):
        """
        Initializes the Logger with the provided output, log level, format, and rotation.
        The output can be a file path, a string, a file object, or a callable.
        The log level is one of the Levels enum values (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        The format is a string that defines the log message format.
        The rotation is an optional parameter that determines when the log file should be rotated.
        
        It can be one of the following:
        - A string representing a time interval (e.g., "1 day", "2 hours", "30 minutes")
        - An integer representing the maximum number of bytes before rotation
        - A date object representing the date when rotation should occur
        - A callable that returns a boolean indicating whether rotation should occur
        """
        
        self._options = (output, level, format, rotation)
        
    def format_log_message(self, context: 'Context', message: str) -> str:
        """
        Formats the log message with the provided context and message.

        :param context: The context of the log message.
        :param message: The log message itself.
        :return: The formatted log message with styles applied.
        """
        
        format_with_colors = self._options[2] if self._options[0] is not sys.stdout else self.format_colors(self._options[2])
        
        
        for color in Colors:
            format_with_colors = format_with_colors.replace(f"<{color.name}>", "")
            format_with_colors = format_with_colors.replace(f"<{color.name.lower()}>", "")
            format_with_colors = format_with_colors.replace(f"<{color.name.capitalize()}>", "")
            
        for style in TextStyles:
            format_with_colors = format_with_colors.replace(f"<{style.name}>", "")
            format_with_colors = format_with_colors.replace(f"<{style.name.lower()}>", "")
            format_with_colors = format_with_colors.replace(f"<{style.name.capitalize()}>", "")

        # Ensure the format string is correctly processed
        formatted_message = format_with_colors.format(
            timestamp=context.timestamp if context.timestamp is not None else '',
            level=context.level.name if context.level is not None else '',
            message=context.message if context.message is not None else '',
            function=context.function if context.function is not None else '',
            file=context.file if context.file is not None else '',
            line=context.line if context.line is not None else '',
            thread=context.thread_id if context.thread_id is not None else ''
        )
        
        return formatted_message
    
    def format_colors(self, format: str) -> str:
        for color in Colors:
            format = format.replace(f"<{color.name}>", color.value).replace(f"<{color.name.lower()}>", color.value).replace(f"<{color.name.capitalize()}>", color.value)

        for style in TextStyles:
            format = format.replace(f"<{style.name}>", style.value).replace(f"<{style.name.lower()}>", style.value).replace(f"<{style.name.capitalize()}>", style.value)
        
        return format
        
    def change(self, *, output: typing.TextIO | typing.BinaryIO | None = None, level: Levels | None = None, format: str | None = None, rotation: AcceptableRotations | None = None) -> None:
        """
        Changes the output, log level, format, and rotation of the Logger.

        :param output: The new output for the Logger.
        :param level: The new log level for the Logger.
        :param format: The new log message format for the Logger.
        :param rotation: The new rotation for the Logger.
        """

        if output is not None:
            self._options = (output, level or self._options[1], format or self._options[2], rotation or self._options[3])
        else:
            self._options = (self._options[0], level or self._options[1], format or self._options[2], rotation or self._options[3])
        
    def debug(self, message: str, exception: typing.Optional[Exception] = None, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None) -> None:
        """
        Logs a message at the DEBUG level.

        :param message: The log message itself.
        :param exception: The exception to be logged, if any.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        """
        context = Context(message, Levels.DEBUG, datetime.now(), function, file, line, thread_id, exception)
        self._write_log(message, context, Levels.DEBUG)

    def info(self, message: str, exception: typing.Optional[Exception] = None, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None) -> None:
        """
        Logs a message at the INFO level.

        :param message: The log message itself.
        :param exception: The exception to be logged, if any.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        """
        context = Context(message, Levels.INFO, datetime.now(), function, file, line, thread_id, exception)
        self._write_log(message, context, Levels.INFO)

    def warning(self, message: str, exception: typing.Optional[Exception] = None, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None) -> None:
        """
        Logs a message at the WARNING level.

        :param message: The log message itself.
        :param exception: The exception to be logged, if any.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        """
        context = Context(message, Levels.WARNING, datetime.now(), function, file, line, thread_id, exception)
        self._write_log(message, context, Levels.WARNING)

    def error(self, message: str, exception: typing.Optional[Exception] = None, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None) -> None:
        """
        Logs a message at the ERROR level.

        :param message: The log message itself.
        :param exception: The exception to be logged, if any.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        """
        context = Context(message, Levels.ERROR, datetime.now(), function, file, line, thread_id, exception)
        self._write_log(message, context, Levels.ERROR)

    def critical(self, message: str, exception: typing.Optional[Exception] = None, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None) -> None:
        """
        Logs a message at the CRITICAL level.

        :param message: The log message itself.
        :param exception: The exception to be logged, if any.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        """
        context = Context(message, Levels.CRITICAL, datetime.now(), function, file, line, thread_id, exception)
        self._write_log(message, context, Levels.CRITICAL)

    def _write_log(self, message: str, context: 'Context', level: Levels) -> None:
        """
        Writes the log message to the output.

        :param message: The log message itself.
        :param context: The context of the log message.
        :param lev el: The level of the log message.
        """
        formatted_message = self.format_log_message(context, message)
        self._options[0].write(formatted_message + '\n')  
        self._options[0].flush()
        
class Context:
    def __init__(self, message: str, level: Levels, timestamp: datetime, function: typing.Optional[str] = None, file: typing.Optional[str] = None, line: typing.Optional[int] = None, thread_id: typing.Optional[int] = None, exception: typing.Optional[Exception] = None):
        """
        Initializes the Context with the provided information about the log message.

        :param message: The log message itself.
        :param level: The level of the log message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        :param timestamp: The timestamp when the log message was generated.
        :param function: The name of the function where the log message was generated.
        :param file: The file path where the log message was generated.
        :param line: The line number in the file where the log message was generated.
        :param thread_id: The ID of the thread that generated the log message.
        :param exception: The exception that was caught, if any.
        """
        self.message = message
        self.level = level
        self.timestamp = timestamp
        self.function = function
        self.file = file
        self.line = line
        self.thread_id = thread_id
        self.exception = exception