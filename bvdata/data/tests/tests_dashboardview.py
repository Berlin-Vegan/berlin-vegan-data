from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.tests.factories import GastroFactory
from bvdata.data.tests.utils import ClientLoginMixin
from bvdata.data.views import DashboardView


class TestDashboardView(ClientLoginMixin, TestCase):
    view_name = "data:dashboard"

    def test_login_required(self):
        response = Client().get(reverse(self.view_name))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"""{reverse("data:login")}?next=/dashboard/""")

    def test_sanity(self):
        response = self.client.get(reverse(self.view_name))
        self.assertEqual(response.status_code, 200)

    def test_queryset(self):
        GastroFactory()
        GastroFactory(closed=None)

        gastro_list = DashboardView().get_queryset()
        for gastro in gastro_list:
            self.assertEqual(gastro.closed, None)
