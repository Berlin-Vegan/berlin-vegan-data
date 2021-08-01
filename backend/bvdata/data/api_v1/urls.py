from django.urls import include, path
from rest_registration.api.views import change_password, login, logout, profile

account_urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("change-password/", change_password, name="change-password"),
]


urlpatterns = [
    path("accounts/", include(account_urlpatterns)),
]
