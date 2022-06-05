from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Question, Choice


# Create your views here.
def get_current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {}.</body></html>".format(now)
    return HttpResponse(html)


def index(request, age=32, year=2021):
    lastest_question_list = Question.objects.order_by('-pubDate')[:5]
    # output = ', '.join([each.questionText for each in lastest_question_list])
    template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': lastest_question_list
    }
    # return HttpResponse(template.render(context, request))
    ## Shortcut
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question doesn't exist...")

    # Shortcut
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'poll/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/result.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    q = Question.objects.get(pk=question_id)
    try:
        choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {
            'question': q,
            'error_message': "You don't select a choice"
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('poll:result', args=(q.id, )))


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # return Question.objects.order_by("-pubDate")[:5]
        return Question.objects.filter(pubDate__lte=timezone.now()).order_by("-pubDate")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pubDate__lte=timezone.now())
