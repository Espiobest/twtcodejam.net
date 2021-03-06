# Generated by Django 3.1.1 on 2020-10-05 20:59

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('timathon', '0007_auto_20201006_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='github_link',
            field=models.CharField(help_text='Link to github repo', max_length=200, validators=[django.core.validators.RegexValidator(regex=re.compile('https://github.com/[A-Za-z0-9-+_.]*/[A-Za-z0-9.+_-]*'))]),
        ),
    ]
