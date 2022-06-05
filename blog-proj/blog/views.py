from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from taggit.models import Tag
from django.db.models import Count


def postList(request, tagSlug=None):
    tag = None
    posts = models.Post.objects.all()
    if tagSlug:
        tag = get_object_or_404(Tag, slug=tagSlug)
        posts = posts.filter(tags__in=[tag,])
    # 4 articles per page
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    # returns the first page if the page number is not an integer
    except PageNotAnInteger:
        posts = paginator.page(1)
    # returns to the last page if the number of pages exceeds the total number of pages
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'page': page, 'posts': posts, 'tag': tag})


def postDetail(request, year, month, day, post):
    post = get_object_or_404(
        models.Post,
        slug=post,
    )
        # status='published',
        # publish__year=year,
        # publish__month=month,
        # publish__day=day)
    comments = post.comments.filter(active=True)

    # Additional new comments
    newComment = None
    if request.method == 'POST':
        commentForm = CommentForm(data=request.POST)
        if commentForm.is_valid():
            # Create new data objects directly from the form, but do not save them to the database
            newComment = commentForm.save(commit=False)
            # Sets the foreign key to the current article
            newComment.post = post
            # Writes the comment data object to the database
            # The save method only works for ModelForm because the Form class is not associated with any data model.
            newComment.save()
    else:
        commentForm = CommentForm()
    # List of similar posts
    postTagsIds = post.tags.values_list('id', flat=True)
    similarTags = models.Post.objects.filter(tags__in=postTagsIds).exclude(id=post.id)
    similarPosts = similarTags.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/detail.html', {'post': post, 'comments':comments, 'newComment':newComment, 'commentForm': commentForm, 'similarPosts':similarPosts})


def postShare(request, postId):
    post = get_object_or_404(models.Post, id = postId, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            postUrl = request.build_absolute_uri(post.getAbsoluteUrl())
            subject = '{} ({}) recommends you reading {}'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, postUrl, cd['name'], cd['comments'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
        sent = False
    return render(request, 'blog/share.html',  {'post': post, 'form':form, 'sent': sent})