from django import forms
from django.urls import reverse
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
            Row(Column('publisher'), Column('location'), css_class='form-row'),
            Row(Column('year'), Column(Field('month', css_class="alt", style="padding: 20px;",))),
            Row(Column('journal'),Column('journal_abbreviation'), Column('volume'),Column('number'),),
            'pages',
            "book_title",
            'institution',
            Row(Column('pdf'),Column('media_public'),),
            'url',
            Row(Column('doi'),Column('isbn'),),
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
        add_publication_url = reverse("publications:publication_add")
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('publication', css_class="alt")),
                Column(HTML(f"<label>&nbsp;</label><br><a href='{add_publication_url}' class='btn btn-primary'>Add Publication</a>")),
                css_class='form-row',
            ),
            Row('locator',css_class='form-row'),
            Field('content_type', type="hidden"),
            Field('object_id', type="hidden"),
            Submit('submit', 'Save'),
        )
        self.helper.form_tag

    def clean(self):
        return super().clean()
