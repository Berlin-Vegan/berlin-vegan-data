import random
from datetime import datetime
from itertools import chain
from typing import Dict, List

from django.test import TestCase

from bvdata.data.api_v2.serializers import (
    GastroAttributeSerializer,
    GastroDetailSerializer,
    OpeningHoursSerializer,
    ShoppingAttributeSerializer,
    ShoppingDetailSerializer,
    TagListSerializer,
)
from bvdata.data.models import (
    GASTRO_BOOLEAN_ATTRIBUTE_CHOICES,
    GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    GASTRO_TAG_CHOICES,
    SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES,
    SHOPPING_TAG_CHOICES,
    BaseLocation,
    LocationTypeChoices,
    Tag,
    WeekdayChoices,
)
from bvdata.data.tests.factories import (
    BaseLocationFactory,
    OpeningHoursFactory,
    TagFactory,
)


def opening_hours_fixture() -> Dict:
    return {
        WeekdayChoices.MONDAY.lower(): dict(
            opening=datetime.now().time(), closing=datetime.now().time()
        ),
        WeekdayChoices.TUESDAY.lower(): dict(
            opening=None, closing=datetime.now().time()
        ),
    }


def tags_input_fixture(choices) -> List[str]:
    return [tag[0] for tag in choices]


def shopping_tags_input_fixture() -> List[str]:
    return tags_input_fixture(SHOPPING_TAG_CHOICES)


def gastro_tags_input_fixture() -> List[str]:
    return tags_input_fixture(GASTRO_TAG_CHOICES)


def shopping_attribute_input_fixture() -> dict:
    states = [True, False, None]
    return {
        attribute[0]: random.choice(states)
        for attribute in SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES
    }


def gastro_attribute_input_fixture() -> dict:
    states_boolean = [True, False, None]
    return {
        **{
            attribute[0]: random.choice(states_boolean)
            for attribute in GASTRO_BOOLEAN_ATTRIBUTE_CHOICES
        },
        **{
            attribute[0]: random.randint(0, 2147483647)
            for attribute in GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES
        },
    }


def baselocation_input_fixture(
    opening_hours_input=None, tags_input=None, attribute_input=None, **kwargs
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
        closed=location_factory.closed,
        text_intern=location_factory.text_intern,
        review=None,
    )
    if attribute_input is not None:
        location_input["attributes"] = attribute_input
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


class TestTagListSerializer(TestCase):
    def test_to_representation_empty(self) -> None:
        self.assertEqual(
            TagListSerializer(tags=SHOPPING_TAG_CHOICES, instance=[]).data, []
        )

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
        self.assertEqual(
            TagListSerializer(tags=SHOPPING_TAG_CHOICES, instance=tags).data,
            expected_data,
        )

    def test_to_internal_value_sanity(self) -> None:
        input_tags = [tag[0] for tag in SHOPPING_TAG_CHOICES]
        serializer = TagListSerializer(tags=SHOPPING_TAG_CHOICES, data=input_tags)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(len(serializer.validated_data), len(SHOPPING_TAG_CHOICES))
        for tag in input_tags:
            self.assertTrue(tag in serializer.validated_data)

    def test_to_internal_value_remove_duplicates(self) -> None:
        input_tags = list(
            chain.from_iterable((tag[0], tag[0]) for tag in SHOPPING_TAG_CHOICES)
        )
        serializer = TagListSerializer(tags=SHOPPING_TAG_CHOICES, data=input_tags)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(len(serializer.validated_data), len(SHOPPING_TAG_CHOICES))


class TestShoppingAttributeSerializer(TestCase):
    def test_to_representation_empty(self) -> None:
        expected_data = {
            attribute[0]: None for attribute in SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES
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
    def test_create_basic(self) -> None:
        location_input = baselocation_input_fixture()
        serializer = ShoppingDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        serializer.validated_data["type"] = LocationTypeChoices.SHOPPING
        instance_serializer = serializer.save()
        self.assertEqual(len(instance_serializer.openinghours_set.all()), 0)
        self.assertEqual(len(instance_serializer.boolean_attributes.all()), 0)
        self.assertEqual(len(instance_serializer.tags.all()), 0)

    def test_create_all(self) -> None:
        location_input = baselocation_input_fixture(
            opening_hours_input=opening_hours_fixture(),
            tags_input=shopping_tags_input_fixture(),
            attribute_input=shopping_attribute_input_fixture(),
        )
        serializer = ShoppingDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        serializer.validated_data["type"] = LocationTypeChoices.SHOPPING
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
        instance = BaseLocationFactory(type=LocationTypeChoices.SHOPPING)
        location_input = baselocation_input_fixture(
            opening_hours_input=opening_hours_fixture(),
            attribute_input=shopping_attribute_input_fixture(),
            tags_input=shopping_tags_input_fixture(),
        )
        serializer = ShoppingDetailSerializer(instance=instance, data=location_input)
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


class TestGastroAttributeSerializer(TestCase):
    def test_to_representation_empty(self) -> None:
        test_object = type("test_object", (object,), {})()
        test_object.boolean_attributes = {}
        test_object.positive_integer_attributes = {}
        expected_data = {
            **{attribute[0]: None for attribute in GASTRO_BOOLEAN_ATTRIBUTE_CHOICES},
            **{
                attribute[0]: 0
                for attribute in GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES
            },
        }
        data_default = GastroAttributeSerializer(instance=test_object).data
        self.assertDictEqual(data_default, expected_data)

    def test_to_internal_value(self) -> None:
        input_attributes = gastro_attribute_input_fixture()
        serializer = GastroAttributeSerializer(data=input_attributes)
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(2, len(validated_data))
        self.assertEqual(
            len(GASTRO_BOOLEAN_ATTRIBUTE_CHOICES),
            len(validated_data["boolean_attributes"]),
        )
        self.assertEqual(
            len(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES),
            len(validated_data["positive_integer_attributes"]),
        )

        for attr in [
            *validated_data["boolean_attributes"],
            *validated_data["positive_integer_attributes"],
        ]:
            self.assertEqual(attr["state"], input_attributes[attr["name"]])


class TestGastroDetailSerializer(TestCase):
    def test_create_basic(self) -> None:
        location_input = baselocation_input_fixture()
        serializer = GastroDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        serializer.validated_data["type"] = LocationTypeChoices.GASTRO
        instance_serializer = serializer.save()
        self.assertEqual(len(instance_serializer.openinghours_set.all()), 0)
        self.assertEqual(len(instance_serializer.boolean_attributes.all()), 0)
        self.assertEqual(len(instance_serializer.tags.all()), 0)

    def test_create_all(self) -> None:
        location_input = baselocation_input_fixture(
            opening_hours_input=opening_hours_fixture(),
            tags_input=gastro_tags_input_fixture(),
            attribute_input=gastro_attribute_input_fixture(),
        )
        serializer = GastroDetailSerializer(data=location_input)
        self.assertTrue(serializer.is_valid())
        serializer.validated_data["type"] = LocationTypeChoices.GASTRO
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
        positive_integer_attributes = instance.positive_integer_attributes.all()
        self.assertEqual(
            len(boolean_attributes) + len(positive_integer_attributes),
            len(location_input["attributes"]),
        )

        for attr in [*boolean_attributes, *positive_integer_attributes]:
            self.assertEqual(
                location_input["attributes"][attr.name],
                attr.state,
            )

        # tags
        tags = instance.tags.all()
        self.assertEqual(len(tags), len(location_input["tags"]))
        for tag in tags:
            self.assertTrue(tag.tag in location_input["tags"])

    def test_update(self) -> None:
        instance = BaseLocationFactory(type=LocationTypeChoices.GASTRO)
        location_input = baselocation_input_fixture(
            opening_hours_input=opening_hours_fixture(),
            attribute_input=gastro_attribute_input_fixture(),
            tags_input=gastro_tags_input_fixture(),
        )
        serializer = GastroDetailSerializer(instance=instance, data=location_input)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        for key, value in location_input.items():
            if key == "tags":
                self.assertEqual(updated_instance.tags.all().count(), len(value))
            elif key == "attributes":
                self.assertEqual(
                    updated_instance.boolean_attributes.all().count()
                    + updated_instance.positive_integer_attributes.all().count(),
                    len(value),
                )
            elif key == "opening_hours":
                self.assertEqual(
                    updated_instance.openinghours_set.all().count(), len(value)
                )
            else:
                self.assertEqual(getattr(updated_instance, key), value)
