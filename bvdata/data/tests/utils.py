from django.contrib.auth import get_user_model
from django.test import Client


def get_form_data(factory, form) -> dict:
    gastro = factory.build()
    return {field_name: getattr(gastro, field_name) for field_name in form.Meta.fields}


def create_gastro_form_data(factory, form) -> dict:
    data = get_form_data(factory=factory, form=form)
    data["handicappedAccessible"] = ""
    data["handicappedAccessibleWc"] = ""
    data["dog"] = ""
    data["organic"] = ""
    data["wlan"] = ""
    data["brunch"] = ""
    data["glutenFree"] = ""
    data["childChair"] = ""
    data["catering"] = ""
    data["breakfast"] = ""
    data["delivery"] = ""
    return data


class ClientLoginMixin:
    login_view_name = "data:login"

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username="test")
        self.client = Client()
        self.client.force_login(user=self.user)
