from enum import Enum, auto

class TextStyles(Enum):
    """
    This class provides a collection of ANSI escape codes for styling text in the console.
    It includes codes for common styles such as underline, bold, italics, strikethrough, double underline, normal, and inverse.
    """
    
    UNDERLINE = u'\033[4m'
    BOLD = u'\033[1m'
    ITALICS = u'\033[3m'
    STRIKETHROUGH = u'\033[9m'
    DOUBLE = u'\033[21m'
    NORMAL = u'\033[0m'
    INVERSE = u'\033[7m'
    FAINT = u'\033[2m'
