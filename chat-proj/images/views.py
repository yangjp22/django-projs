from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCreateForm
from .models import Image
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

@login_required
def imageCreate(request):
    if request.method == 'POST':
        imageForm = ImageCreateForm(request.POST)
        if imageForm.is_valid():
            cd = imageForm.cleaned_data
            newItem = imageForm.save(commit=False)
            newItem.user = request.user
            newItem.save()
            messages.success(request, 'Image added successfully')
            return redirect(newItem.getAbsoluteUrl())
    else:
        imageForm = ImageCreateForm()
    return render(request, 'image/create.html', {'section':'images', 'imageForm': imageForm})

@login_required
def imageDetail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'image/detail.html', {'image': image})

@ajax_required
@login_required
@require_POST
def imageLike(request):
    imageId = request.POST.get('id')
    action = request.POST.get('action')
    if imageId and action:
        try:
            image = Image.objects.get(id=imageId)
            if action == 'like':
                image.usersLike.add(request.user)
            else:
                image.usersLike.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'no'})


def imageList(request):
    images = Image.objects.order_by('title')
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'image/listAjax.html', {'images': images, 'section':'images'})
    return render(request, 'image/list.html', {'images':images, 'section':'images'})

