from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def index(request):
    return HttpResponse("Hello index in view app")


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("In MyView class")