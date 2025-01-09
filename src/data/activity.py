from dataclasses import dataclass
from typing import Self, Union

from src.enums import ActivityStatus, ActivityType


@dataclass
class Activity():
    label: str
    activity_type: ActivityType
    status: ActivityStatus


class ActivityDataExamples():
    DEFAULT_LABEL: str = "Dummy activity"

    @classmethod
    def minimal_input_tuple(cls: Self) -> tuple[str]:
        return cls.DEFAULT_LABEL,

    @classmethod
    def minimal_input_dict(cls: Self) -> dict[str, str]:
        return {
            'label': cls.DEFAULT_LABEL
        }

    @classmethod
    def all_inputs_as_default_tuple(cls: Self) -> tuple[str, ActivityType, ActivityStatus]:
        return (
            cls.DEFAULT_LABEL, 
            ActivityType.get_default_option(),
            ActivityStatus.get_default_option(),
        )

    @classmethod
    def all_inputs_as_default_dict(cls: Self) -> dict[str, Union[str, ActivityType, ActivityStatus]]:
        return {
            'label': cls.DEFAULT_LABEL,
            'activity_type': ActivityType.get_default_option(),
            'status': ActivityStatus.get_default_option(),
        }

    @classmethod
    def all_inputs_random_values_tuple(cls: Self) -> tuple[str, ActivityType, ActivityStatus]:
        return (
            cls.DEFAULT_LABEL, 
            ActivityType.get_default_option(),
            ActivityStatus.get_default_option(),
        )

    @classmethod
    def all_inputs_random_values_dict(cls: Self) -> dict[str, Union[str, ActivityType, ActivityStatus]]:
        return {
            'label': cls.DEFAULT_LABEL,
            'activity_type': ActivityType.get_default_option(),
            'status': ActivityStatus.get_default_option(),
        }
