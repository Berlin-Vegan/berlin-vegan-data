from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bvdata.data.api_v2.viewsets import ShoppingViewSet

router_v2 = DefaultRouter()
router_v2.register(r"shopping", ShoppingViewSet, basename="api-v2-shopping")

urlpatterns = [path("", include(router_v2.urls))]
