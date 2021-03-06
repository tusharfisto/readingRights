# Generated by Django 2.1.4 on 2021-08-16 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_status', models.CharField(max_length=50)),
                ('item_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='userSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userTable',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='grocery',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.userTable'),
        ),
    ]
