from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UploadFileForm
from .utils import handleUploadedFile

# Create your views here.
def index(request):
    return HttpResponse("hellow files")


def uploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handleUploadedFile(form.cleaned_data['files'])
            # return HttpResponseRedirect('/file/upload/success/')
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'files/upload.html', {form: form})


def success(reqeust):
    return HttpResponse("Save successfully...")