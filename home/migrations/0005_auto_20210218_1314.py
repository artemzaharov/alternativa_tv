# Generated by Django 3.1.6 on 2021-02-18 13:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210218_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='why_we',
            field=wagtail.core.fields.StreamField([('Why_we', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Иконка', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Заголовок', required=False)), ('information', wagtail.core.blocks.TextBlock(help_text='Информация', required=False))]))], blank=True, null=True),
        ),
    ]