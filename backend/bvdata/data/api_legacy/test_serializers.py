from django.test import TestCase

from bvdata.data.api_legacy.serializers import (
    GASTRO_DATA_FIELD_NAME_TO_FIELD_NAME,
    OPENING_HOUR_FIELD_NAME,
    _build_base,
)
from bvdata.data.models import VEGAN_VEGAN, LocationTypeChoices, WeekdayChoices
from bvdata.data.tests.factories import BaseLocationFactory, OpeningHoursFactory


class TestSerializers(TestCase):
    def test_closed_location_to_dict(self):
        location = BaseLocationFactory(
            type=LocationTypeChoices.GASTRO,
            vegan=VEGAN_VEGAN,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.MONDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.TUESDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.WEDNESDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.THURSDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.FRIDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.SATURDAY,
        )
        OpeningHoursFactory(
            location=location,
            weekday=WeekdayChoices.SUNDAY,
        )

        location_dict = _build_base(
            location=location, data_to_field_name=GASTRO_DATA_FIELD_NAME_TO_FIELD_NAME
        )
        self.assertEqual(
            f"{location.name} - GESCHLOSSEN / CLOSED", location_dict["name"]
        )
        self.assertNotIn("telephone", location_dict)

        for _, legacy_key in OPENING_HOUR_FIELD_NAME.items():
            self.assertEqual("", location_dict[legacy_key])
