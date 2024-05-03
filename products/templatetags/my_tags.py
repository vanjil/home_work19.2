from django import template

register = template.Library()


@register.filter
def media_filter(photo):
    return photo.url
