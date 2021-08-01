from datetime import datetime as dt

from django.test import TestCase

from bvdata.data.filters import BaseLocationFilter
from bvdata.data.models import BaseLocation
from bvdata.data.tests.factories import BaseLocationFactory


class TestGastroFilter(TestCase):
    def test_is_closed_filter_base_location(self) -> None:
        BaseLocationFactory(closed=None)
        BaseLocationFactory(closed=dt.now())
        qs = BaseLocation.objects.all()
        closed_filter = BaseLocationFilter(data=dict(closed=True), queryset=qs)
        self.assertEqual(closed_filter.qs.count(), 1)

    def test_is_not_closed_filter_base_location(self) -> None:
        BaseLocationFactory(closed=None)
        BaseLocationFactory(closed=dt.now())
        qs = BaseLocation.objects.all()
        closed_filter = BaseLocationFilter(data=dict(closed=False), queryset=qs)
        self.assertEqual(closed_filter.qs.count(), 1)
