from django import template
from ..models import Menu
from wagtail import hooks

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return Menu.objects.none()

