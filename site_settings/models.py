from django.db import models
from wagtail.admin.panels import FieldPanel, TitleFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from autoslug import AutoSlugField
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

@register_setting
class FooterContent(BaseSiteSetting):
    title = models.TextField(
        blank=True,
        help_text="Enter Footer Content Title here",
    )
    content = RichTextField(
        blank=True,
        null=True,
        features=[]
    )
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
        default="slug"
    )

    panels = [
        TitleFieldPanel("title"),
        FieldPanel("slug"),
        FieldPanel("content"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_content")
        cache.delete(key)
        return super().save(*args, **kwargs)

@register_setting
class EmailSettings(BaseSiteSetting):
    email = models.EmailField(
        blank=True,
        help_text="Enter your Email Address here"
    )
    show_email = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("email"),
        FieldPanel("show_email")
    ]
    def save(self, *args, **kwargs):
        key = make_template_fragment_key("email_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    github = models.URLField(
        blank=True,
        help_text="Enter your GitHub URL"
    )
    linkedin = models.URLField(
        blank=True,
        help_text="Enter your LinkedIn URL"
    )
    facebook = models.URLField(
        blank=True,
        help_text="Enter your Facebook URL"
    )
    instagram = models.URLField(
        blank=True,
        help_text="Enter your Instagram URL"
    )

    panels = [
        FieldPanel("github"),
        FieldPanel("linkedin"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
    ]
    def save(self, *args, **kwargs):
        key = make_template_fragment_key("social_media_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)
