from enum import Enum, auto
from typing import Self
import random

class ActivityStatus(Enum):
    PENDING = 0
    OPEN = auto()
    PAUSED = auto()
    CANCELLED = auto()
    CLOSED = auto()

    @classmethod
    def get_default_option(cls: Self) -> Self:
        return cls.OPEN


class ActivityType(Enum):
    COMMON= 0
    MEETING= auto()
    REQUEST= auto()
    TICKET= auto()
    MINOR_PROJECT= auto()
    MAJOR_PROJECT= auto()
    TRAINING= auto()

    @classmethod
    def get_default_option(cls: Self) -> Self:
        return cls.TICKET

if __name__ == "__main__":
    print(type(ActivityStatus.get_default_option()))
    print(ActivityStatus.get_default_option())
    print(type(ActivityType.get_default_option()))
    print(ActivityType.get_default_option())