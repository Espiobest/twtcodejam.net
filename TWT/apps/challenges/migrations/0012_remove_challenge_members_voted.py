# Generated by Django 3.1.1 on 2020-10-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0011_auto_20201005_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='members_voted',
        ),
    ]