__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Robert Turnbull <rob@robturnbull.com>'
__docformat__ = 'epytext'


from django.contrib.contenttypes.fields import GenericRelation

from .reference import Reference

class ReferenceModel(models.Model):
    """ The subject of a citation. """
    references = GenericRelation(Reference)

    class Meta:
        abstract = True
