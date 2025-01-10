from typing import Self
from src.enums import ActivityStatus, ActivityType
from src.errors import (
    InvalidActivityStatusOptionError,
    InvalidActivityTypeOptionError
)

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
        input_message = "Enter status:"
        for item in ActivityStatus:
            input_message += f'\n {item.value}: {item.name.lower().capitalize()}'
        input_message += '\n> '
        status_input: str = input(input_message)
        status_input = status_input.strip()
        if not status_input.isnumeric():
            raise ValueError("Entered option is not a number")
        status_num = int(status_input)
        if status_num not in [s.value for s in ActivityStatus]:
            raise InvalidActivityStatusOptionError('Status option invalid')
        return status_num

    @classmethod
    def ask_type_input(cls: Self) -> int:
        input_message = "Enter type:"
        for item in ActivityStatus:
            input_message += f'\n {item.value}: {item.name.lower().capitalize()}'
        input_message += '\n> '
        status_input: str = input(input_message)
        status_input = status_input.strip()
        if not status_input.isnumeric():
            raise ValueError("Entered option is not a number")
        status_num = int(status_input)
        if status_num not in [s.value for s in ActivityType]:
            raise InvalidActivityTypeOptionError('Status option invalid')
        return status_num
