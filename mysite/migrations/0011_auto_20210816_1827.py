# Generated by Django 2.1.4 on 2021-08-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_usergr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergr',
            name='username',
        ),
        migrations.DeleteModel(
            name='usergr',
        ),
    ]