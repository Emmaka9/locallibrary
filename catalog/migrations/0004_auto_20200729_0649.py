# Generated by Django 2.1.5 on 2020-07-29 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='borrowed',
            field=models.DateField(blank=True, default=datetime.date(2020, 7, 29), null=True, verbose_name='borrowed date'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science Fiction)', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
