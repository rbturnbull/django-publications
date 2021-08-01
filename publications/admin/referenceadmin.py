__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Robert Turnbull <robert.turnbull@unimelb.edu.au>'
__docformat__ = 'epytext'

from django.contrib import admin
from publications.models import Reference

class ReferenceAdmin(admin.ModelAdmin):
	pass