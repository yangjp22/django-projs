from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from . import forms
from .models import Publisher, Books


# Create your views here.
def index(request):
    return HttpResponse("Hello index in view-form")


class MyFormView(View):
    form_name = forms.MyForm
    initial_value = {'key': 'value'}
    template_file = 'viewform/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_name(initial=self.initial_value)
        return render(request, self.template_file, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, self.template_file, {'form': form})


class PublisherListView(ListView):
    model = Publisher
    template_name = 'viewform/publisher.html'
    context_object_name = 'publishers'
    queryset = Books.objects.all()
        
        