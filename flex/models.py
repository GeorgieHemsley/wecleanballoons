from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from streams import blocks
from home.models import new_table_options
from wagtail.blocks import RichTextBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock

class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonials.html",
        )),
        ("pricing_table", blocks.PricingTableBlock(
            table_options=new_table_options
            )),
            ("richtext", RichTextBlock(
                template = "streams/simple_rich_text_block.html",
                features=["bold", "italic", "ol", "ul", "hr", "link"]
            )),
            ("large_image", ImageChooserBlock(
                help_text="This image will be cropped to 1000px by 775px",
                template="streams/large_image_block.html"
            )),
            ("custom_page", PageChooserBlock(
                help_text="Choose an internal page",
                template="streams/custom_page.html"
            ))
    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"
        

