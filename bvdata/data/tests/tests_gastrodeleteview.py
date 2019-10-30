from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from bvdata.data.models import Gastro
from bvdata.data.tests.factories import GastroFactory


class TestGastroDeleteView(TestCase):
    view_name = "data:gastro-delete"

    def test_login_required(self):
        gastro = GastroFactory()
        response = Client().get(reverse(self.view_name, args=[gastro.id_string]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"""{reverse("data:login")}?next={reverse(self.view_name, args=[gastro.id_string])}""",
        )

    def test_delete(self):
        user = get_user_model().objects.create_user(username="test")
        client = Client()
        client.force_login(user=user)
        gastro = GastroFactory()
        self.assertIsNotNone(Gastro.objects.get(id_string=gastro.id_string))
        response = client.post(reverse(self.view_name, args=[gastro.id_string]))
        self.assertEqual(response.url, f"""{reverse("data:dashboard")}""")
        self.assertEqual(len(Gastro.objects.filter(id_string=gastro.id_string)), 0)
