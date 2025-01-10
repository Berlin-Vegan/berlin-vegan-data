import json

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from bvdata.data.api_legacy.serializers import build_gastro, build_shopping
from bvdata.data.forms import GastroSubmitForm
from bvdata.data.mail import mail_new_submit
from bvdata.data.models import BaseLocation, LocationTypeChoices


class GastroSubmitView(CreateView):
    model = BaseLocation
    template_name = "data/gastro-submit.html"
    form_class = GastroSubmitForm

    extra_context_data = {
        "page_name": "gastro-submit",
        "page_title": _("gastro submit"),
    }

    def get_context_data(self, **kwargs):
        return super(GastroSubmitView, self).get_context_data(
            **self.extra_context_data, **kwargs
        )

    def form_valid(self, form):
        form.save()
        submits = BaseLocation.objects.filter(is_submission=True).count()
        mail_new_submit(submits)
        return HttpResponseRedirect(
            "https://www.berlin-vegan.de/submit-danke-thank-you/"
        )


class ApiLocationsJsonMixin:
    location_type = None
    serializer = None

    def get_queryset(self):
        return (
            BaseLocation.objects.api_public()
            .alphabetical()
            .prefetch_related(
                "tags",
                "boolean_attributes",
                "positive_integer_attributes",
                "openinghours_set",
            )
            .filter(type=self.location_type)
        )

    def get_serializer(self):
        return self.serializer

    def get(self, request, *args, **kwargs):
        results = [
            self.serializer(location, request) for location in self.get_queryset()
        ]
        return HttpResponse(json.dumps(results), content_type="application/json")


class ApiGastroLocationsJson(ApiLocationsJsonMixin, ListView):
    location_type = LocationTypeChoices.GASTRO
    serializer = staticmethod(build_gastro)


class ApiShoppingLocationsJson(ApiLocationsJsonMixin, ListView):
    location_type = LocationTypeChoices.SHOPPING
    serializer = staticmethod(build_shopping)
