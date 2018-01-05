import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, RedirectView, CreateView

from bvdata.data.forms import GastroForm
from .models import Gastro


class HomeView(RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'dashboard'


# AuthMixin
class AuthMixin(LoginRequiredMixin):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'


# AuthViews
class DashboardView(AuthMixin, ListView):
    model = Gastro
    template_name = 'data/dashboard.html'
    context_object_name = 'gastros'

    extra_context_data = {
        'page_name': 'dashboard',
        'page_title': _('dashboard'),
    }

    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )


class GastroUpdateView(AuthMixin, UpdateView):
    model = Gastro
    template_name = 'data/gastro-edit.html'
    context_object_name = 'gastro'
    form_class = GastroForm

    extra_context_data = {
        'page_name': 'gastro-edit',
        'page_title': _('gastro edit'),
    }

    def get_context_data(self, **kwargs):
        return super(GastroUpdateView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )

    def get_object(self, queryset=None):
        return get_object_or_404(Gastro, id_string=self.kwargs['id_string'])


class GastroNewView(AuthMixin, CreateView):
    model = Gastro
    template_name = 'data/gastro-new.html'
    form_class = GastroForm

    extra_context_data = {
        'page_name': 'gastro-new',
        'page_title': _('gastro new'),
    }

    def get_context_data(self, **kwargs):
        return super(GastroNewView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )


class ApiGastroLocationsJson(ListView):
    model = Gastro

    def get_queryset(self):
        return Gastro.objects.filter(closed=False)

    def get(self, request, *args, **kwargs):
        results = [gastro.as_dict() for gastro in self.get_queryset()]
        return HttpResponse(json.dumps(results), content_type="application/json")
