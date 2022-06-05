from django.db import models
from django.forms import ModelForm


# Create your models here.
TITLE_CHOICE = [
    ("MR", "Mr."),
    ("MRS", "Mrs."),
    ("MS", "Ms.")
]

class Author(models.Model):
    name = models.CharField(max_length=20)
    titile = models.CharField(choices=TITLE_CHOICE, max_length=3)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        # fields = '__all__'
        # exclude = ['title']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


# author = Author("John")
# form = AuthorForm(request.POST, instance=author)
# form.save()