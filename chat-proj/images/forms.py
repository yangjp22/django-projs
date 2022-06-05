from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description',)
        # widgets = {
        #     'url': forms.HiddenInput,
        # }
        labels = {
            'url': 'Image url (.jpg/.jpeg/)',
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        validExtentions = ['jpg', 'jpeg', 'png',]
        extention = url.strip().rsplit('.', 1)[1].lower()
        if not extention in validExtentions:
            raise forms.ValidationError('The given url does not match valid image extentions')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        imageUrl = self.cleaned_data['url']
        imageName = '{}.{}'.format(slugify(image.title), imageUrl.strip().rsplit('.', 1)[1].lower())
        response = requests.get(imageUrl).content
        image.image.save(imageName, ContentFile(response), save=False)
        if commit:
            image.save()
        return image



