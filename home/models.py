from wagtail.core.models import Page
from django.db import models
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.images.edit_handlers import ImageChooserPanel


class FormField(AbstractFormField):
    page = ParentalKey('HomePage', related_name='custom_form_fields')


class HomePage(AbstractEmailForm, Page):
    # left menu
    item1 = models.CharField(max_length=255, blank=True,
                             help_text='пункт меню 1')
    item2 = models.CharField(max_length=255, blank=True,
                             help_text='пункт меню 2')
    item3 = models.CharField(max_length=255, blank=True,
                             help_text='пункт меню 3')
    item4 = models.CharField(max_length=255, blank=True,
                             help_text='пункт меню 4')
    # first screen
    company_name = models.CharField(
        max_length=255, blank=True, help_text='Название компании')
    decription = models.CharField(
        max_length=255, blank=True, help_text='Описание компании')
    # second screen
    what_we_can = StreamField(
        [
            ('What_we_can', blocks.WeCanBlock())
        ],
        null=True,
        blank=True,
    )
    why_we_title = models.CharField(
        max_length=255, blank=True, help_text='Заголовок почему мы')
    why_we = StreamField(
        [
            ('Why_we', blocks.WhyWeBlock())
        ],
        null=True,
        blank=True,
    )
    button_name = models.CharField(
        max_length=255, blank=True, help_text='Кнопка Блоггерам')

    contact_title = models.CharField(
        max_length=255, blank=True, help_text='Заголовок Контакты')

    contacts_text = models.CharField(
        max_length=255, blank=True, help_text='Текс под заголовком')
    
    contacts = StreamField(
        [
            ('Contacts', blocks.ContactBlock())
        ],
        null=True,
        blank=True,
    )

    social_title = models.CharField(
        max_length=255, blank=True, help_text='Заголовок соц сетей')

    social = StreamField(
        [
            ('Contacts', blocks.SocialBlock())
        ],
        null=True,
        blank=True,
    )

    footer_text = models.CharField(
        max_length=255, blank=True, help_text='Все права защищены....')

    # form with email sends
    template = "home/home_page.html"
    landing_page_template = "home/home_page_landing.html"
    thank_you_text = models.CharField(
        max_length=255, blank=True, help_text='Текст после отправки формы обратной связи (Спасибо мы с вами свяжемся....)')
    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        FieldPanel('item1', classname="full"),
        FieldPanel('item2', classname="full"),
        FieldPanel('item3', classname="full"),
        FieldPanel('item4', classname="full"),
        FieldPanel('company_name', classname="full"),
        FieldPanel('decription', classname="full"),
        StreamFieldPanel('what_we_can'),
        StreamFieldPanel('why_we'),
        FieldPanel('button_name', classname="full"),
        FieldPanel('contact_title', classname="full"),
        FieldPanel('contacts_text', classname="full"),
        StreamFieldPanel('contacts'),
        FieldPanel('social_title', classname="full"),
        StreamFieldPanel('social'),
        FieldPanel('footer_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()


class FlexPage(Page):
    template = "home/flex_page.html"
    description = models.CharField(max_length=255, blank=True, help_text='Заголовок') 
    flex_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Большое фото'
        )
    text = models.TextField(blank=True, help_text='Текст после картинки')
    pluses = models.CharField(max_length=255, blank=True, help_text='Что мы предлагаем') 
    plus_list = StreamField(
        [
            ('Plus', blocks.PlusBlock())
        ],
        null=True,
        blank=True,
    )
    last_text = models.TextField(blank=True, help_text='Текст внизу')
    footer_text = models.CharField(
        max_length=255, blank=True, help_text='Все права защищены....')


    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        ImageChooserPanel('flex_image'),
        FieldPanel('text', classname="full"),
        FieldPanel('pluses', classname="full"),
        StreamFieldPanel('plus_list'),
        FieldPanel('last_text', classname="full"),
        FieldPanel('footer_text', classname="full"),
    ]