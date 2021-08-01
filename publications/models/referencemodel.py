__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Robert Turnbull <rob@robturnbull.com>'
__docformat__ = 'epytext'

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from .reference import Reference

class ReferenceModel(models.Model):
    """ The subject of a citation. """
    references = GenericRelation(Reference)

    class Meta:
        abstract = True

    @cached_property
    def content_type(self):
        return ContentType.objects.get_for_model(self)

    @cached_property
    def content_type_id(self):
        return self.content_type.id

    def add_ref(self, publication, locator=""):
        reference = self.references.filter(publication=publication, locator=locator).first()
        if not reference:
            reference = self.references.create(publication=publication, locator=locator)
        
        return reference

    def add_ref_url(self):
        base_url = reverse('publications:reference_add')
        return f"{base_url}?contenttype={self.content_type_id}&pk={self.id}"