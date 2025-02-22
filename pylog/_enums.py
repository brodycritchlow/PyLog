from enum import Enum, auto
from typing import Any

class Levels(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()

    def __lt__(self, other: 'Levels') -> bool:
        return self.value < other.value

    def __le__(self, other: 'Levels') -> bool:
        return self.value <= other.value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Levels):
            return False
        return self is other

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, Levels):
            return True
        return self is not other

    def __gt__(self, other: 'Levels') -> bool:
        return self.value > other.value

    def __ge__(self, other: 'Levels') -> bool:
        return self.value >= other.value