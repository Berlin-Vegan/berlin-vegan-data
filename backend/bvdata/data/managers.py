from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils import timezone


class GastroQuerySet(models.QuerySet):
    def api_public(self):
        return self.filter(
            (
                Q(closed__isnull=True)
                | Q(vegan=5, closed__gte=timezone.now() - timedelta(weeks=21))
            )
            & Q(is_submission=False)
        )

    def alphabetical(self):
        return self.order_by(Lower("name"))
