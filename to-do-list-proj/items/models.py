from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Todo(models.Model):
  text = models.CharField(max_length=128)
  addDate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} '.format(self.text)

  def was_added_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.addDate <= now