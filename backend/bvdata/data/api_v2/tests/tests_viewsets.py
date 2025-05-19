from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory

from bvdata.data.api_v2.tests.tests_serializers import baselocation_input_fixture
from bvdata.data.models import LocationTypeChoices
from bvdata.data.tests.factories import BaseLocationFactory

factory = APIRequestFactory()


class TestViewSets(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user", email="user@user.de", password="user"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_shopping_view_anonymouse_can_not_access(self) -> None:
        client = APIClient()

        response_get_list = client.get(reverse("data:api-v2-shopping-list"))
        self.assertEqual(response_get_list.status_code, 403)
        response_post = client.post(
            reverse("data:api-v2-shopping-list"), data={}, format="json"
        )
        self.assertEqual(response_post.status_code, 403)

        location = BaseLocationFactory(
            type=LocationTypeChoices.SHOPPING, is_submission=False, closed=None
        )
        location_url = reverse("data:api-v2-shopping-detail", args=[location.id_string])
        response_get_detail = client.get(location_url)
        self.assertEqual(response_get_detail.status_code, 403)
        response_put = client.put(location_url, data={}, format="json")
        self.assertEqual(response_put.status_code, 403)
        response_patch = client.patch(location_url, data={}, format="json")
        self.assertEqual(response_patch.status_code, 403)
        response_delete = client.delete(location_url)
        self.assertEqual(response_delete.status_code, 403)

    def test_shopping_viewset_create_set_last_editor(self) -> None:
        data = baselocation_input_fixture()
        response = self.client.post(
            reverse("data:api-v2-shopping-list"), data=data, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["lastEditor"], self.user.username)

    def test_shopping_viewset_update_set_last_editor(self) -> None:
        location = BaseLocationFactory(type=LocationTypeChoices.SHOPPING)
        data = baselocation_input_fixture()
        response = self.client.put(
            reverse("data:api-v2-shopping-detail", args=[location.id_string]),
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["lastEditor"], self.user.username)

    def test_gastro_view_anonymouse_can_access_list_detail(self) -> None:
        client = APIClient()

        response_get_list = client.get(reverse("data:api-v2-gastro-list"))
        self.assertEqual(response_get_list.status_code, 403)
        response_post = client.post(
            reverse("data:api-v2-gastro-list"), data={}, format="json"
        )
        self.assertEqual(response_post.status_code, 403)

        location = BaseLocationFactory(
            type=LocationTypeChoices.GASTRO, is_submission=False, closed=None
        )
        location_url = reverse("data:api-v2-gastro-detail", args=[location.id_string])
        response_get_detail = client.get(location_url)
        self.assertEqual(response_get_detail.status_code, 403)
        response_put = client.put(location_url, data={}, format="json")
        self.assertEqual(response_put.status_code, 403)
        response_patch = client.patch(location_url, data={}, format="json")
        self.assertEqual(response_patch.status_code, 403)
        response_delete = client.delete(location_url)
        self.assertEqual(response_delete.status_code, 403)
