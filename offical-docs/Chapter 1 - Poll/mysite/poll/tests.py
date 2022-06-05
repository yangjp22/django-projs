from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question


# Create your tests here.
class QuestionTest(TestCase):

    def test_was_published_recently_with_future_question(self):
    # was_published_recently() returns False for questions whose pub_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_q = Question(pubDate=time)
        self.assertIs(future_q.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
    # was_published_recently() returns False for questions whose pub_date is in the future.
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_q = Question(pubDate=time)
        self.assertIs(old_q.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
    # was_published_recently() returns False for questions whose pub_date is in the future.
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_q = Question(pubDate=time)
        self.assertIs(recent_q.was_published_recently(), True)


def create_question(questionText, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(questionText=questionText, pubDate=time)


class QuestionIndexViewTests(TestCase):
    
    def test_no_question(self):
        response = self.client.get(reverse("poll:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        create_question(questionText="Past question", days=-30)
        response = self.client.get(reverse("poll:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: Past question>"])
    
    def test_future_question(self):
        create_question(questionText="Future question", days=30)
        response = self.client.get(reverse("poll:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        create_question(questionText="Future question", days=30)
        create_question(questionText="Past question", days=-30)
        response = self.client.get(reverse("poll:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: Past question>"])

    def test_two_past_questions(self):
        create_question(questionText="Past question 1", days=-30)
        create_question(questionText="Past question 2", days=-5)
        response = self.client.get(reverse("poll:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: Past question 2>", "<Question: Past question 1>"])
    

class QuestionDetailViewTests(TestCase):
    
    def test_future_question(self):
        future_q = create_question(questionText="Future question", days=5)
        response = self.client.get(reverse("poll:detail", args=(future_q.id,)))
        self.assertEqual(response.status_code, 404)
    
    def test_past_questions(self):
        past_q = create_question(questionText="Past question 1", days=-30)
        response = self.client.get(reverse("poll:detail", args=(past_q.id,)))
        self.assertContains(response, past_q.questionText)


