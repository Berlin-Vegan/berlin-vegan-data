from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.forms import GastroSubmitBaseForm
from bvdata.data.models import GastroSubmit
from bvdata.data.tests.factories import GastroSubmitFactory
from bvdata.data.tests.utils import ClientLoginMixin, create_gastro_form_data


class TestGastroSubmitListView(ClientLoginMixin, TestCase):
    view_name = "data:gastro-submit-edit"

    def test_login_required(self):
        gastro_submit = GastroSubmitFactory()
        response = Client().get(reverse(self.view_name, args=[gastro_submit.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"""{reverse(self.login_view_name)}?next=/gastro-submit/{gastro_submit.id}/edit/""",
        )

    def test_sanity(self):
        gastro_submit = GastroSubmitFactory()
        response = self.client.get(reverse(self.view_name, args=[gastro_submit.id]))
        self.assertEqual(response.status_code, 200)

    def test_save(self):
        gastro_submit = GastroSubmitFactory()
        data = create_gastro_form_data(
            factory=GastroSubmitFactory, form=GastroSubmitBaseForm
        )
        response = self.client.post(
            reverse(self.view_name, args=[gastro_submit.id]), data=data
        )
        self.assertEqual(response.status_code, 302)
        gastro_submit_edited = GastroSubmit.objects.get(id=gastro_submit.id)
        self.assertNotEqual(gastro_submit.name, gastro_submit_edited.name)
