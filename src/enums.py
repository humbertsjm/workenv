from enum import Enum, auto

class ActivityStatus(Enum):
    PENDING = 0
    OPEN = auto()
    PAUSED = auto()
    CANCELLED = auto()
    CLOSED = auto()

    @classmethod
    def get_default_option(cls) -> None:
        return cls.OPEN
