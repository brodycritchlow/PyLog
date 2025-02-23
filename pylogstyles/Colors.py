from enum import Enum, auto

class Colors(Enum):
    """
    This class provides a collection of ANSI escape codes for colors in the console.
    It includes codes for common colors such as black, red, green, yellow, blue, magenta, cyan, and white.
    """
    
    BLACK = u'\033[30m'
    RED = u'\033[31m'
    GREEN = u'\033[32m'
    YELLOW = u'\033[33m'
    BLUE = u'\033[34m'
    MAGENTA = u'\033[35m'
    CYAN = u'\033[36m'
    WHITE = u'\033[37m'
    RESET = u'\033[0m'
