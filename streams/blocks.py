from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks

class WeCanBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text='Фото')
    name = blocks.CharBlock(required=False, help_text='Заголовок')
    about = blocks.TextBlock(required=False, help_text='Информация')
    
    class Meta:
        template = 'streams/we_can.html'
        icon = 'edit'
        label = 'Что мы можем'


class WhyWeBlock(blocks.StructBlock):
    icon = blocks.CharBlock(required=False, help_text='Иконка https://fontawesome.com/icons?s=solid например fa-ad/ /...')
    title = blocks.CharBlock(required=False, help_text='Заголовок')
    information = blocks.TextBlock(required=False, help_text='Информация')
    
    class Meta:
        template = 'streams/why_we.html'
        icon = 'edit'
        label = 'Почему мы'

class ContactBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text='Заголовок')
    information = blocks.TextBlock(required=False, help_text='Информация')
    link = blocks.URLBlock(required=False, help_text='Ссылка (если нужна)')
    
    class Meta:
        template = 'streams/contact.html'
        icon = 'edit'
        label = 'Контакты'

class SocialBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text='Заголовок')
    icon = blocks.CharBlock(required=False, help_text='Например: fa-facebook-f/fa-twitter/fa-instagram/fa-linkedin-in')
    link = blocks.URLBlock(required=False, help_text='Ссылка (если нужна)')
    
    class Meta:
        template = 'streams/social.html'
        icon = 'edit'
        label = 'Соц. Сети'

class PlusBlock(blocks.StructBlock):
    plus = blocks.CharBlock(required=False, help_text='Преимущество')    
    class Meta:
        template = 'streams/plus.html'
        icon = 'edit'
        label = 'Список плюсов'