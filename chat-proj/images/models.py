from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import reverse


class Image(models.Model):
    user = models.ForeignKey(User, related_name='imagesCreated', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='Images/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    usersLike = models.ManyToManyField(User, related_name='imagesLiked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def getAbsoluteUrl(self):
        return reverse('images:detail', args=(self.id, self.slug))

