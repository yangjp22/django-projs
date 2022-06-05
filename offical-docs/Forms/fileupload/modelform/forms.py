import django import forms

from .models import TITLE_CHOICE, Author


class AuthorForm(forms.Model):
    name = forms.CharField(max_length=20)
    title = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICE))
    birth_date = forms.DateField(required=False)


class BookForm(forms.Model):
    name = forms.CharField(max_length=30)
    authors = forms.ModelMultipleChoiceField(queryset=Author.object.all())