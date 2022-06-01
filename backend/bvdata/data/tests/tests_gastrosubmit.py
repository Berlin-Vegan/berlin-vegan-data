from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.forms import GastroSubmitForm
from bvdata.data.models import (
    VEGAN_VEGAN,
    BaseLocation,
    BooleanAttribute,
    PositiveIntegerAttribute,
)


class TestGastroSubmit(TestCase):
    view_name = "data:gastro-submit"

    def test_sanity(self):
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_gastrosubmit_form_is_valid(self) -> None:
        form_data = dict(
            name="Test Restaurant",
            street="Teststraße",
            postal_code="12345",
            city="Berlin",
            latitude=5.555,
            longitude=4.444,
            telephone="012345678",
            website="https://test.de",
            email="test@test.de",
            comment="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_english="English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_public_transport="Public Transport, Lorem ipsum dolor sit amet, consetetur ",
            comment_opening_hours="Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            submit_email="submit@test.de",
            bar=False,
            cafe=True,
            eiscafe=False,
            imbiss=True,
            restaurant=False,
            organic=None,
            delivery=True,
            handicapped_accessible=False,
            handicapped_accessible_wc=None,
            dog=True,
            child_chair=False,
            catering=True,
            wlan=None,
            gluten_free=True,
            breakfast=False,
            brunch=None,
            seats_outdoor=10,
            seats_indoor=20,
        )
        form = GastroSubmitForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_gastrosubmit_view(self) -> None:
        client = Client()
        data = dict(
            name="Test Restaurant",
            street="Teststraße",
            postal_code="12345",
            city="Berlin",
            latitude=5.555,
            longitude=4.444,
            telephone="012345678",
            website="https://test.de",
            email="test@test.de",
            comment="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_english="English, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed ",
            comment_public_transport="Public Transport, Lorem ipsum dolor sit amet, consetetur ",
            comment_opening_hours="Open Comment, Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            submit_email="submit@test.de",
            bar=False,
            cafe=True,
            eiscafe=False,
            imbiss=True,
            restaurant=False,
            organic="",
            delivery=True,
            handicapped_accessible=False,
            handicapped_accessible_wc="",
            dog=True,
            child_chair=False,
            catering=True,
            wlan="",
            gluten_free=True,
            breakfast=False,
            brunch="",
            seats_outdoor=10,
            seats_indoor=20,
        )
        response = client.post(reverse(self.view_name), data=data)
        self.assertEqual(
            response.url, "https://www.berlin-vegan.de/submit-danke-thank-you/"
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(len(BaseLocation.objects.all()), 1)
        self.assertEqual(len(BaseLocation.objects.filter(vegan=VEGAN_VEGAN)), 1)
        self.assertEqual(len(PositiveIntegerAttribute.objects.all()), 2)
        self.assertEqual(len(PositiveIntegerAttribute.objects.filter(state=10)), 1)
        self.assertEqual(len(PositiveIntegerAttribute.objects.filter(state=20)), 1)
        self.assertEqual(len(BooleanAttribute.objects.all()), 11)
        self.assertEqual(len(BooleanAttribute.objects.filter(state=None)), 4)
        self.assertEqual(len(BooleanAttribute.objects.filter(state=True)), 4)
        self.assertEqual(len(BooleanAttribute.objects.filter(state=False)), 3)
