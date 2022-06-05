from .. import models
from django import template
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(name='myTag')
def totalPosts():
    return models.Post.objects.count()

@register.inclusion_tag('blog/latest.html')
def showLatestPosts(count=5):
    latestPosts = models.Post.objects.order_by('-publish')[:count]
    return {'latestPosts': latestPosts}

@register.simple_tag
def getMostCommentedPosts(count=5):
    return models.Post.objects.annotate(totalComments=Count('comments')).order_by('-totalComments')[:count]

@register.filter(name='markdown')
def markdownFormat(text):
    return mark_safe(markdown.markdown(text))








