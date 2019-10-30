from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.tests.factories import GastroSubmitFactory
from bvdata.data.tests.utils import ClientLoginMixin
from bvdata.data.views import GastroSubmitListView


class TestGastroSubmitListView(ClientLoginMixin, TestCase):
    view_name = "data:gastro-submit-list"

    def test_login_required(self):
        response = Client().get(reverse(self.view_name))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"""{reverse(self.login_view_name)}?next=/gastro-submit-list/""",
        )

    def test_sanity(self):
        GastroSubmitFactory()
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_queryset(self):
        GastroSubmitFactory()
        gastro_list = GastroSubmitListView().get_queryset()
        self.assertEqual(len(gastro_list), 1)
