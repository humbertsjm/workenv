import string
import random
from src.enums import ActivityStatus, ActivityType

def get_random_string_from_length(length: int=1) -> str:
    alphabet = string.ascii_letters
    return ''.join([random.choice(alphabet) for x in range(length)])

def get_random_activity_status_option() -> ActivityStatus:
    return random.choice([s for s in ActivityStatus])

def get_non_default_random_activity_status_option() -> ActivityStatus:
    choices = [s for s in ActivityStatus]
    choices.remove(ActivityStatus.get_default_option())
    return random.choice(choices)

def get_random_activity_type_option() -> ActivityType:
    return random.choice([s for s in ActivityType])

def get_non_default_random_activity_type_option() -> ActivityType:
    choices = [s for s in ActivityType]
    choices.remove(ActivityType.get_default_option())
    return random.choice(choices)

if __name__ == "__main__":
    pass
