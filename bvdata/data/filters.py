import django_filters

from bvdata.data.models import Gastro


class GastroFilter(django_filters.FilterSet):
    class Meta:
        model = Gastro
        fields = ["vegan"]
