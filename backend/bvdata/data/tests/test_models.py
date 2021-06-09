from unittest import mock

import pytest
from django.db import IntegrityError
from django.test import TestCase

from bvdata.data.models import SHOPPING_BOOELAN_ATTRIBUTE_CHOICES, WeekdayChoices
from bvdata.data.tests.factories import (
    BaseLocationFactory,
    BooleanAttributesFactory,
    OpeningHoursFactory,
    TagFactory,
)


class TestBaseLocationModel(TestCase):
    @mock.patch("bvdata.data.models.get_random_string_32", return_value="abc")
    def test_save_id_string_always_the_same(self, get_random_mock):
        BaseLocationFactory()
        with pytest.raises(RecursionError):
            BaseLocationFactory()

    def test_id_string_unique(self) -> None:
        BaseLocationFactory(id_string="abc")
        with pytest.raises(IntegrityError):
            BaseLocationFactory(id_string="abc")

    def test_check_constrain_type_valid(self) -> None:
        with pytest.raises(IntegrityError):
            BaseLocationFactory(type="abc")


class TestBooleanAttributeModel(TestCase):
    def test_sanity(self) -> None:
        BooleanAttributesFactory()

    def test_check_constrain_name_valid(self) -> None:
        with pytest.raises(IntegrityError):
            BooleanAttributesFactory(name="abc")

    def test_boolean_attribute_choices(self) -> None:
        for attribute in SHOPPING_BOOELAN_ATTRIBUTE_CHOICES:
            self.assertFalse(" " in attribute[0])
            self.assertTrue(attribute[0].islower())


class TestOpeningHoursModel(TestCase):
    def test_sanity(self) -> None:
        BaseLocationFactory()

    def test_weekday_location_unique_together(self) -> None:
        location = BaseLocationFactory()
        OpeningHoursFactory(location=location, weekday=WeekdayChoices.choices[0][0])

        with pytest.raises(IntegrityError):
            OpeningHoursFactory(location=location, weekday=WeekdayChoices.choices[0][0])

    def test_check_constrain_weekday_valid(self) -> None:
        location = BaseLocationFactory()
        with pytest.raises(IntegrityError):
            OpeningHoursFactory(location=location, weekday="abc")


class TestTagModel(TestCase):
    def test_check_constrain_tag_valid(self) -> None:
        with pytest.raises(IntegrityError):
            TagFactory(tag="abc")
