from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='time_filter')
@stringfilter
def timeDo(time):
    return time.split(' ')[0]


@register.filter(name='Mod')
def divide(value):
    return value % 3