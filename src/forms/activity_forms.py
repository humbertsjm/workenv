from typing import Self
from src.enums import ActivityStatus
from src.errors import InvalidStatusOptionError

class ActivityForm():
    @classmethod
    def ask_label_input(cls: Self) -> str:
        label_input: str = input("Enter label: ")
        label_input = label_input.strip()
        if label_input == "":
            raise ValueError('Label cannot be blank')
        return label_input

    @classmethod
    def ask_status_input(cls: Self) -> int:
        status_input: str = input("""
            Enter status:
        """)
        status_input = status_input.strip()
        if not status_input.isnumeric():
            raise ValueError("Enter option is not a number")
        status_num = int(status_input)
        if status_num not in [s.value for s in ActivityStatus]:
            raise InvalidStatusOptionError('Status option invalid')
        return status_num
