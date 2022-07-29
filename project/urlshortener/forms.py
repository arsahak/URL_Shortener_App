from django import forms
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    expired_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={"type": "date", "class": "form-control form-control-lg", }))

    class Meta:
        model = Shortener

        fields = ('long_url', 'expired_date')


class Custom_urlForm(forms.ModelForm):
    custom_url = forms.URLField(
        widget=forms.TextInput(attrs={"class": "form-control-lg", "placeholder": "Enter Your Custom Link", }))

    class Meta:
        model = Shortener

        fields = ('long_url', 'custom_url')

