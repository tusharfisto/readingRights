# Generated by Django 2.1.4 on 2021-08-16 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_grocery_item_quan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery',
            name='item_quan',
        ),
    ]