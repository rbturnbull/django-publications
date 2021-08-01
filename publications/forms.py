from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field, Fieldset
from crispy_forms.bootstrap import AppendedText
from django.forms.models import formset_factory

from publications.models import Publication, Reference

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
            'pdf',
            'media_public',
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

    def clean(self):
        if 'doi' in self.cleaned_data:
            # Remove common prefixes that people could use when adding in the form
            prefixes_to_remove = ["doi.org/", "https://doi.org/", "http://doi.org/", "doi:"]            
            for prefix in prefixes_to_remove:
                if self.cleaned_data['doi'].startswith(prefix):
                    self.cleaned_data['doi'] = self.cleaned_data['doi'][len(prefix):]

        return super().clean()


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['publication', 'locator', 'content_type', 'object_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Field('publication', css_class="alt"),),
            Row('locator',),
            Field('content_type', type="hidden"),
            Field('object_id', type="hidden"),
            Submit('submit', 'Save'),
        )
        self.helper.form_tag

    def clean(self):
        return super().clean()
