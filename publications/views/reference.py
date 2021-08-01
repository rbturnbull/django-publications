__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Robert Turnbull <rob@robturnbull.com>'
__docformat__ = 'epytext'

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
)
from django.urls import reverse
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from publications.models import Reference
from publications.forms import ReferenceForm


class ReferenceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Reference
    form_class = ReferenceForm
    success_message = "Reference updated successfully!"
    template_name = 'publications/reference_form.html'
    extra_context = dict(form_title="Update Reference")
    permission_required = "publications.update_reference"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reference = context['object']
        context['subject'] = reference.content_object
        context['admin_url'] = reverse("admin:publications_reference_change", kwargs={"object_id":reference.pk})
        return context


class ReferenceCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Reference
    form_class = ReferenceForm
    success_message = "Reference added successfully!"
    template_name = 'publications/reference_form.html'
    extra_context = dict(form_title="Add Reference")
    permission_required = "publications.add_reference"

    def get_content_type_info(self):
        """ Returns a tuple with the subject and content type id. """
        # Get the subject of the reference from the content type
        content_type_id = self.request.GET.get("contenttype")
        pk = self.request.GET.get("pk")

        content_type = get_object_or_404( ContentType, id=content_type_id)
        subject = get_object_or_404( content_type.model_class(), pk=pk )
        return subject, content_type_id

    def get_initial(self):
        initial_data = super().get_initial()
        subject, content_type_id = self.get_content_type_info()
        initial_data['content_type'] = content_type_id
        initial_data['object_id'] = subject.pk 
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'], context['content_type_id'] = self.get_content_type_info()
        return context


class ReferenceDetailView(PermissionRequiredMixin, DetailView):
    model = Reference
    template_name = 'publications/reference_detail.html'
    permission_required = "publications.view_reference"
