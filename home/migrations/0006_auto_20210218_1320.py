# Generated by Django 3.1.6 on 2021-02-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210218_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button_name',
            field=models.CharField(blank=True, help_text='Кнопка Блоггерам', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='why_we_title',
            field=models.CharField(blank=True, help_text='Заголовок почему мы', max_length=255),
        ),
    ]
