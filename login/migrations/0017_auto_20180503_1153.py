# Generated by Django 2.0.4 on 2018-05-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ans',
            name='questid',
        ),
        migrations.RemoveField(
            model_name='ans',
            name='userid',
        ),
    ]
