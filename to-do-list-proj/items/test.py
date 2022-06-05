from django.test import TestCase
from django.utils import timezone
from .models import Todo
import datetime

class TodoModelTests(TestCase):

    def test_was_added_recently(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        oldAdd = Todo(addDate = time)
        self.assertIs(oldAdd.was_added_recently(), False)

    def test_was_added_old(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        newAdd = Todo(addDate=time)
        self.assertIs(newAdd.was_added_recently(), True)