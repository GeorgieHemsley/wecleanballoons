from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import Testimonial


class TestimonialAdmin(SnippetViewSet):
    model = Testimonial
    menu_label = "Testimonials"
    menu_name = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_admin_menu = True
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("quote", "attribution")
    search_fields = ("quote", "attribution")

register_snippet(TestimonialAdmin)

