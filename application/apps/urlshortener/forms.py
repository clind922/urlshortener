from django import forms
from application.apps.urlshortener.models import ShortURL


class ShortURLForm(forms.ModelForm):

    class Meta:
        model = ShortURL
        fields = ('redirect_url',)
