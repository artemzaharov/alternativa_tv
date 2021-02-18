from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks

class WeCanBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text='Фото')
    name = blocks.CharBlock(required=False, help_text='Заголовок')
    about = blocks.TextBlock(required=False, help_text='Информация')
    
    class Meta:
        template = 'streams/we_can.html'
        icon = 'edit'
        label = 'gallery'


class WhyWeBlock(blocks.StructBlock):
    icon = blocks.CharBlock(required=False, help_text='Иконка')
    title = blocks.CharBlock(required=False, help_text='Заголовок')
    information = blocks.TextBlock(required=False, help_text='Информация')
    
    class Meta:
        template = 'streams/why_we.html'
        icon = 'edit'
        label = 'gallery'