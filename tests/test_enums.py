from enum import Enum
from src.enums import ActivityStatus

class TestActivityType():
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
