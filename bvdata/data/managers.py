from datetime import timedelta

from django.db.models import Q
from django.utils import timezone
from django.db import models


class GastroQuerySet(models.QuerySet):
    def api(self):
        return self.filter(Q(closed__isnull=True) | Q(vegan=5, closed__gte=timezone.now() - timedelta(weeks=21)))

    def open(self):
        return self.filter(closed__isnull=True)

    def closed(self):
        return self.filter(closed__isnull=False)

