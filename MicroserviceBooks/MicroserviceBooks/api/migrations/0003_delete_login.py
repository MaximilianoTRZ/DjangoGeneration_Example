# Generated by Django 4.1.1 on 2022-09-27 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]