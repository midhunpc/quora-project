# Generated by Django 2.0.4 on 2018-05-06 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20180504_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='nam',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='logs',
            old_name='sid',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='rollno',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='sid',
            new_name='password',
        ),
    ]
