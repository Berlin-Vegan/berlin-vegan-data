import json

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from bvdata.data.forms import GastroSubmitForm
from bvdata.data.mail import mail_new_submit
from bvdata.data.models import Gastro


class GastroSubmitView(CreateView):
    model = Gastro
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
        submits = Gastro.objects.filter(is_submission=True).count()
        mail_new_submit(submits)
        return HttpResponseRedirect(
            "https://www.berlin-vegan.de/submit-danke-thank-you/"
        )


class ApiGastroLocationsJson(ListView):
    model = Gastro

    def get_queryset(self):
        return Gastro.objects.api_public().alphabetical()

    def get(self, request, *args, **kwargs):
        results = [gastro.as_dict() for gastro in self.get_queryset()]
        return HttpResponse(json.dumps(results), content_type="application/json")
