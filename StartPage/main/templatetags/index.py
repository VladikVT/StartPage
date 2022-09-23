from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter(name='times') 
def times(number):
    return range(number)