from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.tests.factories import GastroFactory
from bvdata.data.tests.utils import ClientLoginMixin
from bvdata.data.views import GastrosClosedView


class TestGastroClosedView(ClientLoginMixin, TestCase):
    view_name = "data:gastros-closed"

    def test_login_required(self):
        response = Client().get(reverse(self.view_name))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"""{reverse(self.login_view_name)}?next=/gastros-closed/"""
        )

    def test_sanity(self):
        GastroFactory()
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_queryset(self):
        GastroFactory()
        GastroFactory(closed=None)

        gastro_list = GastrosClosedView().get_queryset()
        for gastro in gastro_list:
            self.assertNotEqual(gastro.closed, None)
