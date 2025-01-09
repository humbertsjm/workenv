from enum import Enum
from src.enums import ActivityStatus, ActivityType

class TestActivityStatus():
    EXPECTED_ITEMS: dict[str, int] = {
        'PENDING': 0,
        'OPEN': 1,
        'PAUSED': 2,
        'CANCELLED': 3,
        'CLOSED': 4,
    }

    def test_is_enum(self) -> None:
        assert issubclass(ActivityStatus, Enum)

    def test_enum_has_all_items(self) -> None:
        for item in self.EXPECTED_ITEMS:
            assert item in [item.name for item in ActivityStatus]

    def test_enum_values_are_correct(self) -> None:
        for item in ActivityStatus:
            assert item.value == self.EXPECTED_ITEMS.get(item.name)

    def test_default_option_function(self) -> None:
        assert ActivityStatus.get_default_option() == ActivityStatus.OPEN

class TestActivityType():
    EXPECTED_ITEMS: dict[str, int] = {
        'COMMON': 0,
        'MEETING': 1,
        'REQUEST': 2,
        'TICKET': 3,
        'MINOR_PROJECT': 4,
        'MAJOR_PROJECT': 5,
        'TRAINING': 6,
    }

    def test_is_enum(self) -> None:
        assert issubclass(ActivityType, Enum)

    def test_enum_has_all_items(self) -> None:
        for item in self.EXPECTED_ITEMS:
            assert item in [item.name for item in ActivityType]

    def test_enum_values_are_correct(self) -> None:
        for item in ActivityType:
            assert item.value == self.EXPECTED_ITEMS.get(item.name)

    def test_default_option_function(self) -> None:
        assert ActivityType.get_default_option() == ActivityType.TICKET
