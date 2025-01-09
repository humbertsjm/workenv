from dataclasses import dataclass
from src.enums import ActivityStatus, ActivityType

@dataclass
class Activity():
    label: str
    activity_type: ActivityType
    status: ActivityStatus
