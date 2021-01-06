from django.contrib.contenttypes.fields import GenericRelation

from .reference import Reference

class ReferenceModel(models.Model):
    """ The subject of a citation. """
    references = GenericRelation(Reference)

    class Meta:
        abstract = True
