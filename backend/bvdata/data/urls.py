from django.urls import include, path

from .api_v1.urls import urlpatterns as v1_urlpatterns
from .views import ApiGastroLocationsJson, GastroSubmitView

app_name = "data"

urlpatterns = [
    path(
        "api/GastroLocations.json", ApiGastroLocationsJson.as_view(), name="api-legacy"
    ),
    path("gastro-submit/", GastroSubmitView.as_view(), name="gastro-submit"),
    path("api/v1/", include(v1_urlpatterns)),
]
