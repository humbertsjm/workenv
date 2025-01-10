import pytest
from pytest import MonkeyPatch
from src.factories.activity_factory import ActivityFactory
from src.data.activity import Activity, ActivityDataExamples
from src.forms.activity_forms import ActivityForm
from src.enums import ActivityStatus, ActivityType
from tests.utils import get_random_string_from_length, get_random_activity_status_option
import random
from src.errors import InvalidStatusOptionError

class TestActivityFactory():
    def test_returns_activity_from_minimal_input(self) -> None:
        data_tuple = ActivityDataExamples.minimal_input_tuple()
        data_dict = ActivityDataExamples.minimal_input_dict()
        activity: Activity = ActivityFactory.create(*data_tuple)
        assert isinstance(activity, Activity)
        assert activity.label == data_tuple[0]
        assert activity.activity_type == ActivityType.get_default_option()
        assert activity.status == ActivityStatus.get_default_option()

        activity: Activity = ActivityFactory.create(**data_dict)
        assert isinstance(activity, Activity)
        assert activity.label == data_dict.get('label')
        assert activity.activity_type == ActivityType.get_default_option()
        assert activity.status == ActivityStatus.get_default_option()

    def test_returns_activity_from_all_inputs(self) -> None:
        data_tuple = ActivityDataExamples.all_inputs_as_default_tuple()
        data_dict = ActivityDataExamples.all_inputs_as_default_dict()
        activity: Activity = ActivityFactory.create(*data_tuple)
        assert isinstance(activity, Activity)
        assert activity.label == data_tuple[0]
        assert activity.activity_type == data_tuple[1]
        assert activity.status == data_tuple[2]

        activity: Activity = ActivityFactory.create(**data_dict)
        assert isinstance(activity, Activity)
        assert activity.label == data_dict.get('label')
        assert activity.activity_type == data_dict.get('activity_type')
        assert activity.status == data_dict.get('status')


class TestActivitiyForms():
    def test_ask_label(self, monkeypatch: MonkeyPatch) -> None:
        random_str = get_random_string_from_length(5)
        monkeypatch.setattr(
            'builtins.input', 
            lambda _: random_str
        )
        asked_input: str = ActivityForm.ask_label_input()
        assert isinstance(asked_input, str)
        assert asked_input == random_str

    def test_empty_ask_label(self, monkeypatch: MonkeyPatch) -> None:
        blank_str = ''
        monkeypatch.setattr(
            'builtins.input', 
            lambda _: blank_str
        )
        with pytest.raises(ValueError):
            asked_input = ActivityForm.ask_label_input()
            assert asked_input == blank_str

    def test_ask_status(self, monkeypatch: MonkeyPatch) -> None:
        random_status: int = get_random_activity_status_option().value
        monkeypatch.setattr(
            'builtins.input', 
            lambda _: str(random_status)
        )
        asked_input: int = ActivityForm.ask_status_input()
        assert isinstance(asked_input, int)
        assert asked_input == random_status

    def test_string_ask_status(self, monkeypatch: MonkeyPatch) -> None:
        random_str = get_random_string_from_length(5)
        monkeypatch.setattr(
            'builtins.input', 
            lambda _: random_str
        )
        with pytest.raises(ValueError):
            ActivityForm.ask_status_input()

    def test_invalid_option_ask_status(self, monkeypatch: MonkeyPatch) -> None:
        random_option: set[int] = set(list(range(10)))
        random_option = random_option.difference([s.value for s in ActivityStatus])
        monkeypatch.setattr(
            'builtins.input', 
            lambda _: str(random.choice(list(random_option)))
        )
        with pytest.raises(InvalidStatusOptionError):
            ActivityForm.ask_status_input()
