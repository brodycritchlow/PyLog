import pytest
from pylog import logger
from pylog._enums import Levels
import sys

def test_debug_capture(capfd):
    logger.change(output=sys.stdout, level=Levels.DEBUG)

    logger.debug('This is a debug log message.')

    captured = capfd.readouterr()
    assert 'This is a debug log message.' in captured.out


def test_info_capture(capfd):
    logger.change(output=sys.stdout, level=Levels.INFO)

    logger.info('This is an info log message.')

    captured = capfd.readouterr()
    assert 'This is an info log message.' in captured.out


def test_warning_capture(capfd):
    logger.change(output=sys.stdout, level=Levels.WARNING)

    logger.warning('This is a warning log message.')

    captured = capfd.readouterr()
    assert 'This is a warning log message.' in captured.out


def test_error_capture(capfd):
    logger.change(output=sys.stdout, level=Levels.ERROR)

    logger.error('This is an error log message.')

    captured = capfd.readouterr()
    assert 'This is an error log message.' in captured.out


def test_critical_capture(capfd):
    logger.change(output=sys.stdout, level=Levels.CRITICAL)

    logger.critical('This is a critical log message.')

    captured = capfd.readouterr()
    assert 'This is a critical log message.' in captured.out

def test_info_not_captured(capfd):
    logger.change(output=sys.stdout, level=Levels.DEBUG)

    logger.info('This info log message should not be captured.')

    captured = capfd.readouterr()
    assert 'This info log message should not be captured.' not in captured.out


def test_warning_not_captured(capfd):
    logger.change(output=sys.stdout, level=Levels.INFO)

    logger.warning('This warning log message should not be captured.')

    captured = capfd.readouterr()
    assert 'This warning log message should not be captured.' not in captured.out


def test_error_not_captured(capfd):
    logger.change(output=sys.stdout, level=Levels.WARNING)

    logger.error('This error log message should not be captured.')

    captured = capfd.readouterr()
    assert 'This error log message should not be captured.' not in captured.out


def test_critical_not_captured(capfd):
    logger.change(output=sys.stdout, level=Levels.ERROR)

    logger.critical('This critical log message should not be captured.')

    captured = capfd.readouterr()
    assert 'This critical log message should not be captured.' not in captured.out
