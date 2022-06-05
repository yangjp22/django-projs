from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .forms import NameForm, ContactForm


# Create your views here.
def index(request):
    return HttpResponse("hello init index")


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/initform/thanks/')
    else:
        form = NameForm()

    return render(request, "initform/name.html", {"form": form})


def thanks(request):
    return HttpResponse("Name thanks")


def send_email(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            subject = contact.cleaned_data['subject']
            message = contact.cleaned_data['message']
            sender = contact.cleaned_data['sender']
            cc_myself = contact.cleaned_data['cc_myself']

            recipents = ['initform@example.com']
            if cc_myself:
                recipents.append(sender)
            
            send_mail(subject, message, sender, recipents)
            return HttpResponseRedirect('/initform/thanks')
    
    else:
        contact = ContactForm()
    return render(request, 'initform/contact.html', {'contact': contact})