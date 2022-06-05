from django.db import models
from django.utils import timezone
import datetime


# Create your models here.  
class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        return self.questionText

    def was_published_recently(self):
        now = timezone.now()
        return now > self.pubDate and now - self.pubDate <= datetime.timedelta(days=1)

    was_published_recently.admin_order_field = "pubDate"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText