from django.db.models import BooleanField, Case, Value, When
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from bvdata.data.api_v2.FilterBackend import AuthorizedFilterBackend
from bvdata.data.api_v2.serializers import (
    PrivateBaseLocationListSerializer,
    PrivateGastroDetailSerializer,
    PrivateShoppingDetailSerializer,
    PublicGastroDetailSerializer,
    PublicShoppingDetailSerializer,
)
from bvdata.data.filters import BaseLocationFilter
from bvdata.data.models import BaseLocation, LocationTypeChoices

__all__ = ("ShoppingViewSet", "GastroViewSet")


class BaseLocationModelViewSetMixin:
    location_type = None
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [AuthorizedFilterBackend]
    serializer_class = {"public": None, "private": {"default": None, "list": None}}
    filterset_class = BaseLocationFilter
    lookup_field = "id_string"

    def __init__(self, **kwargs):
        self.queryset = BaseLocation.objects.filter(
            type=self.get_location_type()
        ).alphabetical()
        self.queryset_public = self.queryset.api_public()
        self.queryset_list_private = self.queryset.annotate(
            has_review_link=Case(
                When(review__isnull=True, then=Value(False)),
                default=Value(True),
                output_field=BooleanField(),
            )
        )
        super(BaseLocationModelViewSetMixin, self).__init__(**kwargs)

    def get_location_type(self):
        if self.location_type is None:
            raise Exception("Location type must be set.")
        return self.location_type

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset_public
        else:
            if self.action == "list":
                return self.queryset_list_private
            return super(BaseLocationModelViewSetMixin, self).get_queryset()

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            return self.serializer_class["public"]
        else:
            return self.serializer_class["private"].get(
                self.action, self.serializer_class["private"]["default"]
            )

    def perform_create(self, serializer):
        serializer.validated_data["last_editor"] = self.request.user
        serializer.validated_data["type"] = self.location_type
        super(BaseLocationModelViewSetMixin, self).perform_create(serializer)

    def perform_update(self, serializer):
        serializer.validated_data["last_editor"] = self.request.user
        super(BaseLocationModelViewSetMixin, self).perform_create(serializer)

    def filter_queryset(self, queryset):
        if self.request.user.is_authenticated:
            return super(BaseLocationModelViewSetMixin, self).filter_queryset(queryset)
        return queryset


class ShoppingViewSet(BaseLocationModelViewSetMixin, ModelViewSet):
    location_type = LocationTypeChoices.SHOPPING
    serializer_class = {
        "public": PublicShoppingDetailSerializer,
        "private": {
            "default": PrivateShoppingDetailSerializer,
            "list": PrivateBaseLocationListSerializer,
        },
    }


class GastroViewSet(BaseLocationModelViewSetMixin, ModelViewSet):
    location_type = LocationTypeChoices.GASTRO
    serializer_class = {
        "public": PublicGastroDetailSerializer,
        "private": {
            "default": PrivateGastroDetailSerializer,
            "list": PrivateBaseLocationListSerializer,
        },
    }
