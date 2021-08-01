__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Robert Turnbull <rob@robturnbull.com>'
__docformat__ = 'epytext'

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

from .publication import Publication


class Reference(models.Model):
    """ A link between a Django model object of any type and a publication. """
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    locator = models.CharField(max_length=255, default="", blank=True, help_text="The location in the publication for this reference (i.e. the page number).")

    # See https://docs.djangoproject.com/en/3.1/ref/contrib/contenttypes/
    # https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.content_object} -> {self.publication} @ {self.locator}"

    def publication_with_locator(self):
        return f"{self.publication}, {self.locator}."

    def get_absolute_url(self):
        return reverse('publications:reference_detail', kwargs={"pk": self.pk})

    def get_absolute_update_url(self):
        return reverse('publications:reference_update', kwargs={"pk": self.pk})

    class Meta:
        ordering = ["publication__year", "publication__authors", "locator"]