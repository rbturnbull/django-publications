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
from django.shortcuts import render

from publications.models import Publication
from publications.forms import PublicationForm


class PublicationCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    success_message = "Publication added successfully!"
    template_name = 'publications/form.html'
    extra_context = dict(form_title="Add Publication")
    permission_required = "publications.add_publication"


class PublicationUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Publication
    form_class = PublicationForm
    success_message = "Publication updated successfully!"
    template_name = 'publications/form.html'
    extra_context = dict(form_title="Update Publication")
    slug_field = 'citekey'
    slug_url_kwarg = 'citekey'
    permission_required = "publications.update_publication"


class PublicationDetailView(PermissionRequiredMixin, DetailView):
    model = Publication
    template_name = 'publications/publication_detail.html'
    slug_field = 'citekey'
    slug_url_kwarg = 'citekey'
    permission_required = "publications.view_publication"


class PublicationExportView(PublicationDetailView):
    def get(self, request, *args, **kwargs):
        publication = self.get_object()
        response = render(
            request, 
            f'publications/publication.{self.file_extension}', 
            {'publication': publication}, 
            content_type=self.content_type
        )
        response['Content-Disposition'] = f'attachment; filename="{publication.citekey}.{self.file_extension}"'
        return response


class PublicationRISView(PublicationExportView):
    content_type='application/x-research-info-systems; charset=UTF-8'
    file_extension = "ris"


class PublicationBibtexView(PublicationExportView):
    # content_type='text/x-bibtex; charset=UTF-8'
    content_type='text/html; charset=UTF-8'
    file_extension = "bib"

