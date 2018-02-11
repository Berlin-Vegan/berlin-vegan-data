import json
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, RedirectView, CreateView, DeleteView, DetailView
from rest_framework import viewsets

from bvdata.data.forms import GastroForm, GastroSubmitForm, GastroSubmitEditForm, GastroSubmitCheckForm, \
    GastroModelChoiceForm, GastroModelChoiceRequiredForm, GastroSubmitBaseForm
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
        return HttpResponseRedirect(reverse('data:dashboard'))


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


class GastroSubmitEditView(AuthMixin, DetailView):
    model = GastroSubmit
    template_name = 'data/gastro-submit-edit.html'
    context_object_name = 'gastro_submit'

    extra_context_data = {
        'page_name': 'gastros-submit',
        'page_title': _('gastros-submit'),
    }

    def get_context_data(self, **kwargs):
        gastro_form = GastroSubmitBaseForm()
        submit_edit_form = GastroSubmitEditForm(instance=self.object, prefix='submit')
        submit_edit_check = GastroSubmitCheckForm(prefix='check')
        return super(GastroSubmitEditView, self).get_context_data(
            forms_tupel_list=self.get_tupel_list(gastro_form, submit_edit_form, submit_edit_check),
            gastros_modelchoice=GastroModelChoiceForm(initial=dict(gastros=self.object.gastro), prefix='gastro'),
            **self.extra_context_data,
            **kwargs,
        )

    def get_tupel_list(self, gastro_form, gastro_submit, fastro_submit_check):
        labels = [field.label_tag() for field in gastro_form]
        form_ids = [field.auto_id for field in gastro_form]
        submit_edit_form = gastro_submit
        submit_edit_check = fastro_submit_check
        return list(zip(labels, form_ids, submit_edit_form, submit_edit_check))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        gastro_id_form = GastroModelChoiceRequiredForm(request.POST, prefix='gastro')
        gastro_submit = GastroSubmitEditForm(request.POST, prefix='submit')
        gastro_submit_check = GastroSubmitCheckForm(request.POST, prefix='check')

        if 'create' in request.POST and gastro_submit.is_valid():
            g = Gastro(**gastro_submit.cleaned_data, last_editor=request.user)
            g.save()
            self.object.delete()
            return redirect('data:gastro-update', g.id_string)

        if 'update' in request.POST and gastro_id_form.is_valid() and gastro_submit.is_valid() and gastro_submit_check.is_valid():
            gastro_update = {}
            for field, value in gastro_submit_check.cleaned_data.items():
                if value:
                    gastro_update.update({f'{field}': gastro_submit.cleaned_data[field]})
            gastro_update.update(dict(last_editor=request.user, updated=datetime.now()))
            gastro_instance = gastro_id_form.cleaned_data['gastros']
            Gastro.objects.filter(id=gastro_instance.id).update(**gastro_update)
            self.object.delete()
            return redirect('data:gastro-update', gastro_instance.id_string)

        if 'delete' in request.POST:
            self.object.delete()
            return redirect('data:gastro-submit-list')

        else:
            gastro_form = GastroForm()
            context = super(GastroSubmitEditView, self).get_context_data(
                forms_tupel_list=self.get_tupel_list(gastro_form, gastro_submit, gastro_submit_check),
                gastros_modelchoice=gastro_id_form,
                **self.extra_context_data,
                **kwargs
            )
            return self.render_to_response(context=context)


# api

class ApiGastroLocationsJson(ListView):
    model = Gastro

    def get_queryset(self):
        return Gastro.objects.filter(closed=False)

    def get(self, request, *args, **kwargs):
        results = [gastro.as_dict() for gastro in self.get_queryset()]
        return HttpResponse(json.dumps(results), content_type="application/json")


# restframework

class GastroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gastro.objects.all()
    serializer_class = GastroSerializer
