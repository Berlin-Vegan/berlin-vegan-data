import random
from datetime import datetime
from itertools import chain
from typing import Dict

from django.test import TestCase

from bvdata.data.api_v2.serializers import (
    OpeningHoursSerializer,
    PrivateShoppingDetailSerializer,
    ShoppingAttributeSerializer,
    TagShoppingListSerializer,
)
from bvdata.data.models import (
    SHOPPING_BOOELAN_ATTRIBUTE_CHOICES,
    SHOPPING_TAG_CHOICES,
    BaseLocation,
    Tag,
    WeekdayChoices,
)
from bvdata.data.tests.factories import (
    BaseLocationFactory,
    OpeningHoursFactory,
    TagFactory,
)


def tags_input_fixture():
    return [tag[0] for tag in SHOPPING_TAG_CHOICES]


def shopping_attribute_input_fixture():
    states = [True, False, None]
    return {
        attribute[0]: random.choice(states)
        for attribute in SHOPPING_BOOELAN_ATTRIBUTE_CHOICES
    }


def baselocation_input_fixture(
    opening_hours_input=None, tags_input=None, shopping_attribute_input=None, **kwargs
):
    location_factory = BaseLocationFactory.build(**kwargs)
    location_input = dict(
        name=location_factory.name,
        street=location_factory.street,
        postal_code=location_factory.postal_code,
        city=location_factory.city,
        vegan=location_factory.vegan,
        latitude=location_factory.latitude,
        longitude=location_factory.longitude,
        telephone=location_factory.telephone,
        website=location_factory.website,
        email=location_factory.email,
        comment=location_factory.comment,
        comment_english=location_factory.comment_english,
        comment_opening_hours=location_factory.comment_opening_hours,
        review_link=location_factory.review_link,
        closed=location_factory.closed,
        text_intern=location_factory.text_intern,
    )
    if shopping_attribute_input is not None:
        location_input["attributes"] = shopping_attribute_input
    if tags_input is not None:
        location_input["tags"] = tags_input
    if opening_hours_input is not None:
        location_input["opening_hours"] = opening_hours_input
    return location_input


class TestOpeningHoursSerializer(TestCase):
    def test_to_representation_default(self) -> None:
        expected_data = {
            day[0].lower(): dict(opening=None, closing=None)
            for day in WeekdayChoices.choices
        }

        data_default = OpeningHoursSerializer(instance={}).data
        self.assertDictEqual(data_default, expected_data)

    def test_to_representation_data_exists(self) -> None:
        location = BaseLocationFactory()
        expected_data = {}

        for day in WeekdayChoices.choices:
            opening_hour = OpeningHoursFactory(location=location, weekday=day[0])
            expected_data[opening_hour.weekday.lower()] = dict(
                opening=opening_hour.opening, closing=opening_hour.closing
            )

        data_model_manager = OpeningHoursSerializer(
            instance=location.openinghours_set
        ).data
        self.assertDictEqual(data_model_manager, expected_data)

        data_without_model_manager = OpeningHoursSerializer(
            instance=location.openinghours_set.all()
        ).data
        self.assertDictEqual(data_without_model_manager, expected_data)

    def test_to_internal_value_empty(self):
        input_data = {}
        serializer = OpeningHoursSerializer(data=input_data)
        self.assertTrue(serializer.is_valid())
        self.assertListEqual(serializer.validated_data, [])

    def test_to_internal_exist(self) -> None:
        input_data = {
            WeekdayChoices.MONDAY.lower(): dict(
                opening=datetime.now().time(), closing=datetime.now().time()
            ),
            WeekdayChoices.TUESDAY.lower(): dict(
                opening=None, closing=datetime.now().time()
            ),
            WeekdayChoices.WEDNESDAY.lower(): dict(
                opening=datetime.now().time(), closing=None
            ),
            WeekdayChoices.THURSDAY.lower(): dict(opening=None, closing=None),
            WeekdayChoices.FRIDAY.lower(): dict(),
        }
        serializer = OpeningHoursSerializer(data=input_data)
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertTrue(isinstance(validated_data, list))
        for opening_hour in validated_data:
            self.assertEqual(
                opening_hour["opening"],
                input_data[opening_hour["weekday"].lower()]["opening"],
            )
            self.assertEqual(
                opening_hour["closing"],
                input_data[opening_hour["weekday"].lower()]["closing"],
            )
            self.assertNotEqual(opening_hour["weekday"], WeekdayChoices.FRIDAY)


class TestTagShoppingListSerializer(TestCase):
    def test_to_representation_empty(self) -> None:
        self.assertEqual(TagShoppingListSerializer(instance=[]).data, [])

    def test_to_representation(self) -> None:
        TagFactory(tag=SHOPPING_TAG_CHOICES[0][0])
        TagFactory(tag=SHOPPING_TAG_CHOICES[1][0])
        TagFactory(tag=SHOPPING_TAG_CHOICES[2][0])
        tags = Tag.objects.all()
        expected_data = [
            SHOPPING_TAG_CHOICES[0][0],
            SHOPPING_TAG_CHOICES[1][0],
            SHOPPING_TAG_CHOICES[2][0],
        ]
        self.assertEqual(TagShoppingListSerializer(instance=tags).data, expected_data)

    def test_to_internal_value_sanity(self) -> None:
        input_tags = [tag[0] for tag in SHOPPING_TAG_CHOICES]
        serializer = TagShoppingListSerializer(data=input_tags)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(len(serializer.validated_data), len(SHOPPING_TAG_CHOICES))
        for tag in input_tags:
            self.assertTrue(tag in serializer.validated_data)

    def test_to_internal_value_remove_duplicates(self) -> None:
        input_tags = list(
            chain.from_iterable((tag[0], tag[0]) for tag in SHOPPING_TAG_CHOICES)
        )
        serializer = TagShoppingListSerializer(data=input_tags)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(len(serializer.validated_data), len(SHOPPING_TAG_CHOICES))


class TestShoppingAttributeSerializer(TestCase):
    def test_to_representation_empty(self) -> None:
        expected_data = {
            attribute[0]: None for attribute in SHOPPING_BOOELAN_ATTRIBUTE_CHOICES
        }
        data_default = ShoppingAttributeSerializer(instance={}).data
        self.assertDictEqual(data_default, expected_data)

    def test_to_internal_value(self) -> None:
        input_attributes = shopping_attribute_input_fixture()
        serializer = ShoppingAttributeSerializer(data=input_attributes)
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(len(input_attributes), len(validated_data))
        for key, state in input_attributes.items():
            self.assertIsNotNone(
                next(
                    (
                        item
                        for item in validated_data
                        if item["name"] == key and item["state"] == state
                    ),
                    None,
                )
            )


class TestShoppingDetailSerializer(TestCase):
    @staticmethod
    def opening_hours_fixture() -> Dict:
        return {
            WeekdayChoices.MONDAY.lower(): dict(
                opening=datetime.now().time(), closing=datetime.now().time()
            ),
            WeekdayChoices.TUESDAY.lower(): dict(
                opening=None, closing=datetime.now().time()
            ),
        }

    def test_create_basic(self) -> None:
        location_input = baselocation_input_fixture()
        serializer = PrivateShoppingDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        instance_serializer = serializer.save()
        self.assertEqual(len(instance_serializer.openinghours_set.all()), 0)
        self.assertEqual(len(instance_serializer.boolean_attributes.all()), 0)
        self.assertEqual(len(instance_serializer.tags.all()), 0)

    def test_create_all(self) -> None:
        location_input = baselocation_input_fixture(
            opening_hours_input=self.opening_hours_fixture(),
            tags_input=tags_input_fixture(),
            shopping_attribute_input=shopping_attribute_input_fixture(),
        )
        serializer = PrivateShoppingDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        instance_serializer = serializer.save()
        instance = BaseLocation.objects.get(id_string=instance_serializer.id_string)

        # opening hours
        opening_hours = instance.openinghours_set.all()
        self.assertEqual(len(opening_hours), len(location_input["opening_hours"]))
        for opening_hour in opening_hours:
            opening_hour_input = location_input["opening_hours"][
                opening_hour.weekday.lower()
            ]
            self.assertEqual(opening_hour_input["opening"], opening_hour.opening)
            self.assertEqual(opening_hour_input["closing"], opening_hour.closing)

        # boolean attributes
        boolean_attributes = instance.boolean_attributes.all()
        self.assertEqual(len(boolean_attributes), len(location_input["attributes"]))

        for boolean_attribute in boolean_attributes:
            self.assertEqual(
                location_input["attributes"][boolean_attribute.name],
                boolean_attribute.state,
            )

        # tags
        tags = instance.tags.all()
        self.assertEqual(len(tags), len(location_input["tags"]))
        for tag in tags:
            self.assertTrue(tag.tag in location_input["tags"])

    def test_update(self) -> None:
        instance = BaseLocationFactory()
        location_input = baselocation_input_fixture(
            opening_hours_input=self.opening_hours_fixture(),
            shopping_attribute_input=shopping_attribute_input_fixture(),
            tags_input=tags_input_fixture(),
        )
        serializer = PrivateShoppingDetailSerializer(
            instance=instance, data=location_input
        )
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        for key, value in location_input.items():
            if key == "tags":
                self.assertEqual(updated_instance.tags.all().count(), len(value))
            elif key == "attributes":
                self.assertEqual(
                    updated_instance.boolean_attributes.all().count(), len(value)
                )
            elif key == "opening_hours":
                self.assertEqual(
                    updated_instance.openinghours_set.all().count(), len(value)
                )
            else:
                self.assertEqual(getattr(updated_instance, key), value)
