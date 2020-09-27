from datetime import timedelta

from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from bvdata.data.models import OMNIVORE_VEGAN, VEGAN_VEGAN, Gastro
from bvdata.data.tests.factories import GastroFactory


class TestApiGastroLocationsJson(TestCase):
    view_name = "data:api-legacy"

    def setUp(self) -> None:
        self.client = Client()

    def test_gastro_to_dict(self):
        Gastro.objects.create(
            id_string="6zd67nov4gjk8wv24trgxd9sr1r5f413",
            name="Test Restaurant",
            street="Teststraße",
            postal_code="12345",
            city="Berlin",
            latitude=5.555,
            longitude=4.444,
            telephone="012345678",
            website="https://test.de",
            email="test@test.de",
            opening_mon="09:00:00",
            closing_mon="15:00:00",
            opening_tue="10:00:00",
            closing_tue="16:00:00",
            opening_wed="11:00:00",
            closing_wed="17:00:00",
            opening_thu="12:00:00",
            closing_thu="18:00:00",
            opening_fri="13:00:00",
            closing_fri="19:00:00",
            opening_sat="14:00:00",
            closing_sat="20:00:00",
            opening_sun="15:00:00",
            closing_sun="21:00:00",
            vegan=5,
            comment="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_english="English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            review_link="https://www.berlin-vegan.de/essen-und-trinken/rezensionen/test-restaurant/",
            closed=None,
            text_intern="Intern, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            district="LICHTENBERG",
            public_transport="Public Transport, Lorem ipsum dolor sit amet, consetetur ",
            handicapped_accessible=True,
            handicapped_accessible_wc=False,
            dog=None,
            child_chair=True,
            catering=False,
            delivery=None,
            organic=False,
            wlan=True,
            gluten_free=None,
            breakfast=True,
            brunch=False,
            seats_outdoor=40,
            seats_indoor=50,
            restaurant=True,
            imbiss=False,
            eiscafe=False,
            cafe=True,
            bar=False,
            comment_open="Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            submit_email="submit@test.de",
            has_sticker=True,
            is_submission=False,
        )
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
                "district": "Lichtenberg",
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
                "tags": ["Restaurant", "Cafe"],
                "reviewURL": "test-restaurant",
                "created": timezone.now().strftime("%Y-%m-%d"),
            }
        ]
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), api_fixture)

    def test_no_submission(self) -> None:
        GastroFactory(is_submission=True, closed=None)
        GastroFactory(is_submission=False, closed=None)
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)

    def test_no_closed(self) -> None:
        GastroFactory(is_submission=False, vegan=OMNIVORE_VEGAN)
        GastroFactory(is_submission=False, closed=None)
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)

    def test_no_closed_vegan(self) -> None:
        GastroFactory(
            is_submission=False,
            vegan=VEGAN_VEGAN,
            closed=timezone.now() - timedelta(weeks=22),
        )
        GastroFactory(
            is_submission=False,
            vegan=VEGAN_VEGAN,
            closed=timezone.now() - timedelta(weeks=20, days=6, hours=23),
        )
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(len(response.json()), 1)
