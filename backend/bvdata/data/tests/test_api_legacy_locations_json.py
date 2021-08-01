from datetime import timedelta

from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from bvdata.data.models import (
    OMNIVORE_VEGAN,
    VEGAN_VEGAN,
    BaseLocation,
    BooleanAttribute,
    LocationTypeChoices,
    OpeningHours,
    PositiveIntegerAttribute,
    Tag,
    WeekdayChoices,
)
from bvdata.data.tests.factories import BaseLocationFactory


class TestApiGastroLocationsJson(TestCase):
    view_name = "data:api-gastro-legacy"

    def setUp(self) -> None:
        self.client = Client()

    def test_gastro_to_dict(self):
        location = BaseLocation.objects.create(
            id_string="6zd67nov4gjk8wv24trgxd9sr1r5f413",
            type=LocationTypeChoices.GASTRO,
            name="Test Restaurant",
            street="Teststraße",
            postal_code="12345",
            city="Berlin",
            latitude=5.555,
            longitude=4.444,
            telephone="012345678",
            website="https://test.de",
            email="test@test.de",
            vegan=5,
            comment="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_english="English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            review_link="https://www.berlin-vegan.de/essen-und-trinken/rezensionen/test-restaurant/",
            closed=None,
            text_intern="Intern, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_public_transport="Public Transport, Lorem ipsum dolor sit amet, consetetur ",
            comment_opening_hours="Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            submit_email="submit@test.de",
            has_sticker=True,
            is_submission=False,
        )

        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.MONDAY,
            opening="09:00:00",
            closing="15:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.TUESDAY,
            opening="10:00:00",
            closing="16:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.WEDNESDAY,
            opening="11:00:00",
            closing="17:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.THURSDAY,
            opening="12:00:00",
            closing="18:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.FRIDAY,
            opening="13:00:00",
            closing="19:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.SATURDAY,
            opening="14:00:00",
            closing="20:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.SUNDAY,
            opening="15:00:00",
            closing="21:00:00",
        )

        tags = [Tag.objects.create(tag="cafe"), Tag.objects.create(tag="restaurant")]
        location.tags.set(tags)
        pos_int_attributes = [
            PositiveIntegerAttribute.objects.create(name="seats_outdoor", state=40),
            PositiveIntegerAttribute.objects.create(name="seats_indoor", state=50),
        ]
        location.positive_integer_attributes.set(pos_int_attributes)
        boolean_attributes = [
            BooleanAttribute.objects.create(name="handicapped_accessible", state=True),
            BooleanAttribute.objects.create(
                name="handicapped_accessible_wc", state=False
            ),
            BooleanAttribute.objects.create(name="dog", state=None),
            BooleanAttribute.objects.create(name="child_chair", state=True),
            BooleanAttribute.objects.create(name="catering", state=False),
            BooleanAttribute.objects.create(name="delivery", state=None),
            BooleanAttribute.objects.create(name="organic", state=False),
            BooleanAttribute.objects.create(name="wlan", state=True),
            BooleanAttribute.objects.create(name="gluten_free", state=None),
            BooleanAttribute.objects.create(name="breakfast", state=True),
            BooleanAttribute.objects.create(name="brunch", state=False),
        ]
        location.boolean_attributes.set(boolean_attributes)
        api_fixture = [
            {
                "id": "6zd67nov4gjk8wv24trgxd9sr1r5f413",
                "name": "Test Restaurant",
                "street": "Teststraße",
                "cityCode": "12345",
                "city": "Berlin",
                "latCoord": 5.555,
                "longCoord": 4.444,
                "vegan": 5,
                "district": "Berlin",
                "telephone": "012345678",
                "website": "https://test.de",
                "email": "test@test.de",
                "otMon": "09:00 - 15:00",
                "otTue": "10:00 - 16:00",
                "otWed": "11:00 - 17:00",
                "otThu": "12:00 - 18:00",
                "otFri": "13:00 - 19:00",
                "otSat": "14:00 - 20:00",
                "otSun": "15:00 - 21:00",
                "comment": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
                "commentEnglish": "English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
                "openComment": "Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
                "publicTransport": "Public Transport, Lorem ipsum dolor sit amet, consetetur ",
                "handicappedAccessible": 1,
                "handicappedAccessibleWc": 0,
                "dog": -1,
                "childChair": 1,
                "catering": 0,
                "delivery": -1,
                "organic": 0,
                "wlan": 1,
                "glutenFree": -1,
                "breakfast": 1,
                "brunch": 0,
                "seatsOutdoor": 40,
                "seatsIndoor": 50,
                "tags": ["Cafe", "Restaurant"],
                "reviewURL": "test-restaurant",
                "created": timezone.now().strftime("%Y-%m-%d"),
            }
        ]
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), api_fixture)

    def test_no_submission(self) -> None:
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO, is_submission=True, closed=None
        )
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO, is_submission=False, closed=None
        )
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)

    def test_no_closed(self) -> None:
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO, is_submission=False, vegan=OMNIVORE_VEGAN
        )
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO, is_submission=False, closed=None
        )
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)

    def test_no_closed_vegan(self) -> None:
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO,
            is_submission=False,
            vegan=VEGAN_VEGAN,
            closed=timezone.now() - timedelta(weeks=22),
        )
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO,
            is_submission=False,
            vegan=VEGAN_VEGAN,
            closed=timezone.now() - timedelta(weeks=20, days=6, hours=23),
        )
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)

    def test_only_gastro_type(self) -> None:
        BaseLocationFactory(
            type=LocationTypeChoices.SHOPPING,
            closed=None,
            is_submission=False,
        )
        BaseLocationFactory(
            type=LocationTypeChoices.GASTRO,
            closed=None,
            is_submission=False,
        )
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)


class TestApiShoppingLocationsJson(TestCase):
    view_name = "data:api-shopping-legacy"

    def setUp(self) -> None:
        self.client = Client()

    def test_shopping_to_dict(self):
        location = BaseLocation.objects.create(
            id_string="6zd67nov4gjk8wv24trgxd9sr1r5f413",
            type=LocationTypeChoices.SHOPPING,
            name="Test Shop",
            street="Teststraße",
            postal_code="12345",
            city="Berlin",
            latitude=5.555,
            longitude=4.444,
            telephone="012345678",
            website="https://test.de",
            email="test@test.de",
            vegan=5,
            comment="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_english="English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            review_link="https://www.berlin-vegan.de/essen-und-trinken/rezensionen/test-shop/",
            closed=None,
            text_intern="Intern, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_public_transport="Public Transport, Lorem ipsum dolor sit amet, consetetur ",
            comment_opening_hours="Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            submit_email="submit@test.de",
            has_sticker=True,
            is_submission=False,
        )

        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.MONDAY,
            opening="09:00:00",
            closing="15:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.TUESDAY,
            opening="10:00:00",
            closing="16:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.WEDNESDAY,
            opening="11:00:00",
            closing="17:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.THURSDAY,
            opening="12:00:00",
            closing="18:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.FRIDAY,
            opening="13:00:00",
            closing="19:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.SATURDAY,
            opening="14:00:00",
            closing="20:00:00",
        )
        OpeningHours.objects.create(
            location=location,
            weekday=WeekdayChoices.SUNDAY,
            opening="15:00:00",
            closing="21:00:00",
        )

        tags = [Tag.objects.create(tag="clothing"), Tag.objects.create(tag="foods")]
        location.tags.set(tags)
        boolean_attributes = [
            BooleanAttribute.objects.create(name="handicapped_accessible", state=True),
            BooleanAttribute.objects.create(name="delivery", state=None),
            BooleanAttribute.objects.create(name="organic", state=False),
        ]
        location.boolean_attributes.set(boolean_attributes)
        api_fixture = [
            {
                "id": "6zd67nov4gjk8wv24trgxd9sr1r5f413",
                "name": "Test Shop",
                "street": "Teststraße",
                "cityCode": "12345",
                "city": "Berlin",
                "latCoord": 5.555,
                "longCoord": 4.444,
                "vegan": 5,
                "telephone": "012345678",
                "website": "https://test.de",
                "email": "test@test.de",
                "otMon": "09:00 - 15:00",
                "otTue": "10:00 - 16:00",
                "otWed": "11:00 - 17:00",
                "otThu": "12:00 - 18:00",
                "otFri": "13:00 - 19:00",
                "otSat": "14:00 - 20:00",
                "otSun": "15:00 - 21:00",
                "comment": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
                "commentEnglish": "English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
                "openComment": "Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
                "handicappedAccessible": 1,
                "delivery": -1,
                "organic": 0,
                "tags": ["clothing", "foods"],
                "reviewURL": "test-shop",
            },
        ]
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), api_fixture)
