from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=20)
    files = forms.FileField()