# Generated by Django 2.0.4 on 2018-05-02 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20180502_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='sid',
        ),
    ]
