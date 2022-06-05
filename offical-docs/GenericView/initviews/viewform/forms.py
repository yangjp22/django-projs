from django import forms


class MyForm(forms.Form):
    key = forms.CharField(max_length=20)