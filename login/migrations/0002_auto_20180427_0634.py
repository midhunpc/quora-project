# Generated by Django 2.0.4 on 2018-04-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='rollno',
            field=models.CharField(max_length=100),
        ),
    ]
