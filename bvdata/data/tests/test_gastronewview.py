from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.forms import GastroForm
from bvdata.data.models import Gastro
from bvdata.data.tests.factories import GastroFactory
from bvdata.data.tests.utils import ClientLoginMixin, create_gastro_form_data


class TestGastroNewView(ClientLoginMixin, TestCase):
    view_name = "data:gastro-new"

    def test_login_required(self):
        response = Client().get(reverse(self.view_name))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"""{reverse(self.login_view_name)}?next=/gastro-new/"""
        )

    def test_sanity(self):
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        data = create_gastro_form_data(factory=GastroFactory, form=GastroForm)
        response = self.client.post(reverse(self.view_name), data=data)
        self.assertEqual(response.status_code, 302)
        gastro_new = Gastro.objects.last()
        self.assertEqual(data["name"], gastro_new.name)
        self.assertEqual(gastro_new.last_editor, self.user)
