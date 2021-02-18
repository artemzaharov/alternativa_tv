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
    contacts = models.CharField(
        max_length=255, blank=True, help_text='Контакты')
    contacts_text = models.CharField(
        max_length=255, blank=True, help_text='Текст под Контакты')
    adress = models.CharField(
        max_length=255, blank=True, help_text='Заголовок Адреса')
    adress_text = models.CharField(
        max_length=255, blank=True, help_text='Адрес офиса')
    email = models.CharField(
        max_length=255, blank=True, help_text='Заголовок Емэйл')
    email_text = models.CharField(
        max_length=255, blank=True, help_text='Адрес Емэйл')    
    phone = models.CharField(
        max_length=255, blank=True, help_text='Заголовок Телефон')
    phone_text = models.CharField(
        max_length=255, blank=True, help_text='Номер телефона')
    social = models.CharField(
        max_length=255, blank=True, help_text='Заголовок Соц.Сети')
    social_links = models.CharField(
        max_length=255, blank=True, help_text='Ссылки на соц сети')

    footer_text = models.CharField(
        max_length=255, blank=True, help_text='Все права защищены....')

    # form with email sends
    template = "home/home_page.html"
    landing_page_template = "home/home_page_landing.html"
    thank_you_text = RichTextField(blank=True)
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
        FieldPanel('contacts', classname="full"),
        FieldPanel('contacts_text', classname="full"),
        FieldPanel('adress', classname="full"),
        FieldPanel('adress_text', classname="full"),
        FieldPanel('email', classname="full"),
        FieldPanel('email_text', classname="full"),
        FieldPanel('phone', classname="full"),
        FieldPanel('phone_text', classname="full"),
        FieldPanel('social', classname="full"),
        FieldPanel('social_links', classname="full"),
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
    pass
