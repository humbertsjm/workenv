from src.data.activity import Activity
from src.enums import ActivityStatus

class ActivityFactory:
    @classmethod

    def create(cls, label, status=ActivityStatus.OPEN) -> Activity:
        return Activity(label, status)
