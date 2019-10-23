from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DataConfig(AppConfig):
    name = "bvdata.data"
    verbose_name = _("Data")
