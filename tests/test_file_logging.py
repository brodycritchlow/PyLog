import pytest
from pylog import logger
from pylog._enums import Levels
import io

def test_debug_capture():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.DEBUG)

    logger.debug('This is a debug log message.')

    content = log_stream.getvalue()
    assert 'This is a debug log message.' in content


def test_info_capture():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.INFO)

    logger.info('This is an info log message.')

    content = log_stream.getvalue()
    assert 'This is an info log message.' in content


def test_warning_capture():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.WARNING)

    logger.warning('This is a warning log message.')

    content = log_stream.getvalue()
    assert 'This is a warning log message.' in content


def test_error_capture():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.ERROR)

    logger.error('This is an error log message.')

    content = log_stream.getvalue()
    assert 'This is an error log message.' in content


def test_critical_capture():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.CRITICAL)

    logger.critical('This is a critical log message.')

    content = log_stream.getvalue()
    assert 'This is a critical log message.' in content


def test_info_not_captured():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.DEBUG)

    logger.info('This info log message should not be captured.')

    content = log_stream.getvalue()
    assert 'This info log message should not be captured.' not in content


def test_warning_not_captured():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.INFO)

    logger.warning('This warning log message should not be captured.')

    content = log_stream.getvalue()
    assert 'This warning log message should not be captured.' not in content


def test_error_not_captured():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.WARNING)

    logger.error('This error log message should not be captured.')

    content = log_stream.getvalue()
    assert 'This error log message should not be captured.' not in content


def test_critical_not_captured():
    log_stream = io.StringIO()
    logger.change(output=log_stream, level=Levels.ERROR)

    logger.critical('This critical log message should not be captured.')

    content = log_stream.getvalue()
    assert 'This critical log message should not be captured.' not in content
