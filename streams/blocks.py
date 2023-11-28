from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django import forms
from wagtail.contrib.table_block.blocks import TableBlock
from django.core.exceptions import ValidationError
from django import forms
from wagtail.blocks import StructBlockValidationError
from wagtail.blocks.stream_block import StreamBlockValidationError

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required = True,
        help_text="Text to Display"
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"

class LinkValue(blocks.StructValue):
    # Additional logic for links
    def url(self):
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""

class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50, 
        default="More Detail",
    )
    internal_page = blocks.PageChooserBlock(
        required=False,
    )
    external_link = blocks.URLBlock(
        required=False,
    )

    class Meta:
        value_class = LinkValue
    
    def clean(self, value):
        result = super().clean(value)
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")      
        if internal_page and external_link:
            raise StreamBlockValidationError(
                block_errors=
                {
                    "internal_page": ValidationError("Both links can't be filled, please choose one to use."),
                    "external_link": ValidationError("Both links can't be filled, please choose one to use.")
                })
        if not internal_page and not external_link:
            raise StreamBlockValidationError(
                block_errors=
                {
                    "internal_page": ValidationError("You need to choose a link or a page!"),
                    "external_link": ValidationError("You need to choose a link or a page!")
                }
            )
            
        return result
 
class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100, 
        help_text="Bold title text for this card. Max length of 100 chars",
    )
    text = blocks.TextBlock(
        max_length=255, 
        help_text="Optional text for this card. Max length is 255 chars",
        required=False,
    )
    image = ImageChooserBlock(
        help_text="Image will be automagically cropped to 570px by 370px",
    )
    link = Link(help_text="enter link or select page")
    

class CardsBlock(blocks.StructBlock):
    
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Image automatically cropped to 786px by 552px")
    image_alignment = RadioSelectBlock(
        choices = (
            ("left", "Left"),
            ("right", "Right"),
        ), default="left",
        help_text="Image on the left with text on the right or image on the right with text on the left"
    )
    title = blocks.CharBlock(
        max_length=60,
        help_text="Max length of 60 characters"
    )
    text = blocks.CharBlock(
        max_length=140, 
        help_text="Max lenght 140 characters",
        required=False,
    )
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"

class CallToActionBlock(blocks.StructBlock):

    title = blocks.CharBlock(
        max_length=200,
        help_text="Max length 200 characters"
    )
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "plus"
        label = "Call To Action"

class PricingTableBlock(TableBlock):

    class Meta:
        template = "streams/pricing_table_block.html"
        label = "Pricing Table"
        icon = "table"
        help_text = "Your pricing tables should always have 4 collumns."