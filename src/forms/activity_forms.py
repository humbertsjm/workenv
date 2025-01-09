from typing import Self


class ActivityForm():
    @classmethod
    def ask_label_input(cls: Self) -> str:
        label_input: str = input("Enter label: ")
        label_input = label_input.strip()
        if label_input == "":
            raise ValueError('Label cannot be blank')
        return label_input
