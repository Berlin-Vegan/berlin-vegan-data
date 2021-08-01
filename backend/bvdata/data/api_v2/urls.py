from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bvdata.data.api_v2.viewsets import GastroViewSet, ShoppingViewSet

router_v2 = DefaultRouter()
router_v2.register(r"shopping", ShoppingViewSet, basename="api-v2-shopping")
router_v2.register(r"gastro", GastroViewSet, basename="api-v2-gastro")

urlpatterns = [path("", include(router_v2.urls))]
