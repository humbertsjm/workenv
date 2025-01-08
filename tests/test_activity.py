from src.factories.activity_factory import ActivityFactory
from src.data.activity import Activity
from src.enums import ActivityStatus


class TestActivityFactory():
    # Only label input
    MINIMAL_INPUT_TUPLE: tuple[str] = "Dummy activity",
    MINIMAL_INPUT_DICT: dict[str, str]= {
        'label': 'Dummy activity'
    }

    # All inputs
    ALL_INPUTS_TUPLE: tuple[str, str] = "Dummy activity", ActivityStatus.get_default_option(),
    ALL_INPUTS_DICT: dict[str, str]= {
        'label': 'Dummy activity',
        'status': ActivityStatus.get_default_option()
    }

    def test_returns_activity_from_minimal_input(self) -> None:
        activity: Activity = ActivityFactory.create(*self.MINIMAL_INPUT_TUPLE)
        assert isinstance(activity, Activity)
        assert activity.label == self.MINIMAL_INPUT_TUPLE[0]
        assert activity.status == ActivityStatus.get_default_option()

        activity: Activity = ActivityFactory.create(**self.MINIMAL_INPUT_DICT)
        assert isinstance(activity, Activity)
        assert activity.label == self.MINIMAL_INPUT_DICT.get('label')
        assert activity.status == ActivityStatus.get_default_option()

    def test_returns_activity_from_all_inputs(self) -> None:
        activity: Activity = ActivityFactory.create(*self.ALL_INPUTS_TUPLE)
        assert isinstance(activity, Activity)
        assert activity.label == self.ALL_INPUTS_TUPLE[0]
        assert activity.status == self.ALL_INPUTS_TUPLE[1]

        activity: Activity = ActivityFactory.create(**self.ALL_INPUTS_DICT)
        assert isinstance(activity, Activity)
        assert activity.label == self.ALL_INPUTS_DICT.get('label')
        assert activity.status == self.ALL_INPUTS_DICT.get('status')
