from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . import models

# Create your views here.
def home(request):
    toDoList = models.Todo.objects.all().order_by('-addDate')
    data = {'toDolist': toDoList}
    return render(request, 'item/index.html', data)

@csrf_exempt
def listItem(request):
    item = request.POST.get('item')
    upDate = timezone.now()
    models.Todo.objects.create(addDate=upDate, text=item)
    return redirect('app_item:home')

@csrf_exempt
def deleteItem(request, deleteId):
    models.Todo.objects.get(pk=deleteId).delete()
    return redirect('app_item:home')