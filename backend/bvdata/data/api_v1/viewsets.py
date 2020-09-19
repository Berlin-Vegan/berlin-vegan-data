from django.db.models import BooleanField, Case, Value, When
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from bvdata.data.api_v1.serializers import GastroDetailSerializer, GastroListSerializer
from bvdata.data.filters import GastroFilter
from bvdata.data.models import Gastro


class GastroViewSet(ModelViewSet):
    queryset = Gastro.objects.all().annotate(
        has_review_link=Case(
            When(review_link__exact="", then=Value(False)),
            default=Value(True),
            output_field=BooleanField(),
        )
    )
    serializer_class = GastroDetailSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = GastroFilter
    lookup_field = "id_string"

    def get_serializer_class(self):
        if self.action == "list":
            return GastroListSerializer
        return super(GastroViewSet, self).get_serializer_class()

    def perform_create(self, serializer):
        serializer.validated_data["last_editor"] = self.request.user
        super(GastroViewSet, self).perform_create(serializer)

    def perform_update(self, serializer):
        serializer.validated_data["last_editor"] = self.request.user
        super(GastroViewSet, self).perform_create(serializer)
