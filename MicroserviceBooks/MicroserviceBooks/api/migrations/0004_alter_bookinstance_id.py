# Generated by Django 4.1.1 on 2022-10-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
