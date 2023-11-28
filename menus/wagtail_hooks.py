
from django.db import models
from wagtail import hooks
from .models import Menu
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet


class MenuAdmin(SnippetViewSet):
    model = Menu
    menu_order = 200
    menu_label = "Menus"
    menu_icon = "list-ul"
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    
register_snippet(MenuAdmin)