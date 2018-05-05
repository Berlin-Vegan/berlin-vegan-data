import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, RedirectView, CreateView, DeleteView
from rest_framework import viewsets

from bvdata.data.forms import GastroForm, GastroSubmitForm, UserProfileChangeEmailForm
from bvdata.data.serializer import GastroSerializer
from .models import Gastro, GastroSubmit


class HomeView(RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'data:dashboard'


# AuthMixin
class AuthMixin(LoginRequiredMixin):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'


# AuthViews
class DashboardView(AuthMixin, ListView):
    model = Gastro
    template_name = 'data/dashboard.html'
    context_object_name = 'gastros'

    def get_queryset(self):
        return super(DashboardView, self).get_queryset().open()

    extra_context_data = {
        'page_name': 'dashboard',
        'page_title': _('dashboard'),
    }

    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )


class GastrosClosedView(DashboardView):
    extra_context_data = {
        'page_name': 'gastros-closed',
        'page_title': _('Gastro Closed'),
    }

    def get_queryset(self):
        return super(ListView, self).get_queryset().closed()


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

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.last_editor = self.request.user
        instance.save()
        return super(GastroUpdateView, self).form_valid(form)


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

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.last_editor = self.request.user
        instance.save()
        return super(GastroNewView, self).form_valid(form)


class GastroDeleteView(AuthMixin, DeleteView):
    model = Gastro

    def get_success_url(self):
        return reverse('data:dashboard')

    def get_object(self, queryset=None):
        return get_object_or_404(Gastro, id_string=self.kwargs['id_string'])


class GastroSubmitView(AuthMixin, CreateView):
    model = GastroSubmit
    template_name = 'data/gastro-submit.html'
    form_class = GastroSubmitForm

    extra_context_data = {
        'page_name': 'gastro-submit',
        'page_title': _('gastro submit')
    }

    def get_context_data(self, **kwargs):
        return super(GastroSubmitView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('https://www.berlin-vegan.de/submit-danke-thank-you/')


class GastroSubmitListView(AuthMixin, ListView):
    model = GastroSubmit
    template_name = 'data/gastros-submit-list.html'
    context_object_name = 'gastros_submit'

    extra_context_data = {
        'page_name': 'gastros-submit',
        'page_title': _('gastros-submit'),
    }

    def get_context_data(self, **kwargs):
        return super(GastroSubmitListView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )

    def get_object(self, queryset=None):
        return get_object_or_404(Gastro, id_string=self.kwargs['id_string'])


class GastroSubmitEditView(AuthMixin, CreateView):
    model = Gastro
    template_name = 'data/gastro-submit-edit.html'
    context_object_name = 'gastro_submit'
    form_class = GastroForm

    extra_context_data = {
        'page_name': 'gastros-submit',
        'page_title': _('gastros-submit'),
    }

    def get_gastrosubmit(self):
        return get_object_or_404(GastroSubmit, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        return super(GastroSubmitEditView, self).get_context_data(
            gastro_submit=self.get_gastrosubmit(),
            form=GastroForm(instance=self.get_gastrosubmit()),
            **self.extra_context_data,
            **kwargs,
        )

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.last_editor = self.request.user
        instance.save()
        self.get_gastrosubmit().delete()
        return super(GastroSubmitEditView, self).form_valid(form)


class GastroSubmitDeleteView(AuthMixin, DeleteView):
    model = GastroSubmit

    def get_success_url(self):
        return reverse('data:gastro-submit-list')

    def get_object(self, queryset=None):
        return get_object_or_404(GastroSubmit, id=self.kwargs['id'])


# api
class ApiGastroLocationsJson(ListView):
    model = Gastro

    def get_queryset(self):
        return Gastro.objects.api()

    def get(self, request, *args, **kwargs):
        results = [gastro.as_dict() for gastro in self.get_queryset()]
        return HttpResponse(json.dumps(results), content_type="application/json")


# restframework
class GastroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gastro.objects.all()
    serializer_class = GastroSerializer


# user profile

class UserProfileView(UpdateView):
    model = User
    template_name = 'registration/user-profile.html'
    context_object_name = 'user'
    form_class = UserProfileChangeEmailForm

    extra_context_data = {
        'page_name': 'user-profile',
        'page_title': _('user profile'),
    }

    def get_context_data(self, **kwargs):
        return super(UserProfileView, self).get_context_data(
            **self.extra_context_data,
            **kwargs,
        )

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)

    def get_success_url(self):
        return reverse('data:user-profile')
