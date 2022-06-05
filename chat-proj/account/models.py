from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='User/%Y/%m/%d/', blank=True)

    def __str__(self):
        return "Profile for user {}".format(self.user.username)


class Contract(models.Model):
    # The user who initiated the attention
    userFrom = models.ForeignKey(User, related_name='relFromSet', on_delete=models.CASCADE)
    # The following users
    userTo = models.ForeignKey(User, related_name='relToSet', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return '{} follows {}'.format(self.userFrom, self.userTo)


User.add_to_class('following', models.ManyToManyField('self', through=Contract, related_name='followers', symmetrical=False))










