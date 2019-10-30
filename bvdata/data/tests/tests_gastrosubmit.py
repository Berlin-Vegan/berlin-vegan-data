from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.forms import GastroSubmitForm
from bvdata.data.models import GastroSubmit
from bvdata.data.tests.factories import GastroSubmitFactory
from bvdata.data.tests.utils import create_gastro_form_data, get_form_data


class TestGastroSubmit(TestCase):
    view_name = "data:gastro-submit"

    def test_gastrosubmit_form_is_valid(self) -> None:
        form = GastroSubmitForm(
            data=get_form_data(factory=GastroSubmitFactory, form=GastroSubmitForm)
        )
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(GastroSubmit.objects.all()), 1)

    def test_sanity(self):
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_gastrosubmit_view(self) -> None:
        client = Client()
        data = create_gastro_form_data(
            factory=GastroSubmitFactory, form=GastroSubmitForm
        )
        response = client.post(reverse(self.view_name), data=data)
        self.assertEqual(
            response.url, "https://www.berlin-vegan.de/submit-danke-thank-you/"
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(len(GastroSubmit.objects.all()), 1)
