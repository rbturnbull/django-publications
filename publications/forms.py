from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field, Fieldset
from crispy_forms.bootstrap import AppendedText
from django.forms.models import formset_factory

from publications.models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Fieldset(
            Field('type', css_class="alt"),
            'title',
            'authors',
            Row('publisher', 'location'),
            Row('year', Field('month', css_class="alt", style="padding: 20px;",)),
            Row('journal','journal_abbreviation'),
            Row('volume', 'number'),
            Row('book_title'),
            'pages',
            'institution',
            'url',
            'doi',
            'isbn',
            'note',
            'citekey',
            'abstract',
            'keywords',
            Field('lists',css_class="alt"),
            # ),
            Submit('submit', 'Save')
        )

	# pdf = models.FileField(upload_to='publications/', verbose_name='PDF', blank=True, null=True)
	# image = models.ImageField(upload_to='publications/images/', blank=True, null=True)
	# thumbnail = models.ImageField(upload_to='publications/thumbnails/', blank=True, null=True)
	# lists = models.ManyToManyField(List, blank=True)