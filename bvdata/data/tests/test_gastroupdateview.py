from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.forms import GastroForm
from bvdata.data.models import Gastro
from bvdata.data.tests.factories import GastroFactory
from bvdata.data.tests.utils import ClientLoginMixin, create_gastro_form_data


class TestGastroUpdateView(ClientLoginMixin, TestCase):
    view_name = "data:gastro-update"

    def test_login_required(self):
        gastro = GastroFactory()
        response = Client().get(reverse(self.view_name, args=[gastro.id_string]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"""{reverse(self.login_view_name)}?next=/location/gastro/{gastro.id_string}/edit/""",
        )

    def test_sanity(self):
        gastro = GastroFactory()
        response = self.client.get(
            reverse("data:gastro-update", args=[gastro.id_string])
        )
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        gastro_submit = GastroFactory()
        data = create_gastro_form_data(factory=GastroFactory, form=GastroForm)
        response = self.client.post(
            reverse(self.view_name, args=[gastro_submit.id_string]), data=data
        )
        self.assertEqual(response.status_code, 302)
        gastro_submit_edited = Gastro.objects.get(id_string=gastro_submit.id_string)
        self.assertNotEqual(gastro_submit.name, gastro_submit_edited.name)
        self.assertEqual(gastro_submit_edited.last_editor, self.user)
