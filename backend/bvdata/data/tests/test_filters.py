from datetime import datetime as dt

from django.test import TestCase

from bvdata.data.filters import GastroFilter
from bvdata.data.models import Gastro
from bvdata.data.tests.factories import GastroFactory


class TestGastroFilter(TestCase):
    def test_is_closed_filter(self) -> None:
        GastroFactory(closed=None)
        GastroFactory(closed=None)
        GastroFactory(closed=dt.now())
        qs = Gastro.objects.all()
        closed_filter = GastroFilter(data=dict(closed=True), queryset=qs)
        self.assertEqual(closed_filter.qs.count(), 1)

    def test_is_not_closed_filter(self) -> None:
        GastroFactory(closed=None)
        GastroFactory(closed=dt.now())
        GastroFactory(closed=dt.now())
        qs = Gastro.objects.all()
        closed_filter = GastroFilter(data=dict(closed=False), queryset=qs)
        self.assertEqual(closed_filter.qs.count(), 1)
