from typing import Self
from src.data.activity import Activity
from src.enums import ActivityStatus,ActivityType

class ActivityFactory:
    @classmethod
    def create(
        cls: Self, 
        label, 
        activity_type=ActivityType.get_default_option(),
        status=ActivityStatus.get_default_option(),
    ) -> Activity:
        return Activity(label, activity_type, status)
