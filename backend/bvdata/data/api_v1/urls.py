from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_registration.api.views import change_password, login, logout, profile

from bvdata.data.api_v1.viewsets import GastroViewSet

router_v1 = DefaultRouter()
router_v1.register(r"gastros", GastroViewSet, basename="api-gastros")

account_urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("change-password/", change_password, name="change-password"),
]


urlpatterns = [
    path("", include(router_v1.urls)),
    path("accounts/", include(account_urlpatterns)),
]
