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
    RANDOM_ITERATIONS: int = 1000

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

    def test_random_option(self) -> None:
        assert isinstance(ActivityStatus.get_random_option(), ActivityStatus)
        enum_set: set[int] = set([s.value for s in ActivityStatus])
        random_options: set[int] = set([
            ActivityStatus.get_random_option().value
            for n in range(self.RANDOM_ITERATIONS)
        ])
        assert random_options.issubset(enum_set)
        # Unlikely to be 1
        assert len(random_options) > 1 

    def test_non_default_random_option(self) -> None:
        random_options: set[int] = set([
            ActivityStatus.get_non_default_random_option().value
            for n in range(self.RANDOM_ITERATIONS)
        ])
        # Unlikely to have random option after RANDOM_ITERATIONS iterations
        assert ActivityStatus.get_default_option().value not in random_options

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
