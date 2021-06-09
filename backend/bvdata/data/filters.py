from django_filters import rest_framework as filters

from bvdata.data.models import BaseLocation, Gastro


class GastroFilter(filters.FilterSet):
    closed = filters.BooleanFilter(field_name="closed", method="filter_closed")

    @staticmethod
    def filter_closed(qs, _, value):
        return (
            qs.filter(closed__isnull=False) if value else qs.filter(closed__isnull=True)
        )

    class Meta:
        model = Gastro
        fields = ["closed", "is_submission"]


class BaseLocationFilter(GastroFilter):
    class Meta(GastroFilter.Meta):
        model = BaseLocation
