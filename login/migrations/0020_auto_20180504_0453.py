# Generated by Django 2.0.4 on 2018-05-04 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20180504_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ans',
            name='questid',
            field=models.CharField(max_length=50),
        ),
    ]
