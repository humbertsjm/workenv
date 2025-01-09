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

    @classmethod
    def get_random_option(cls: Self) -> Self:
        return random.choice([s for s in cls])

    @classmethod
    def get_non_default_random_option(cls: Self) -> Self:
        choices = [s for s in cls]
        choices.remove(cls.get_default_option())
        return random.choice(choices)

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