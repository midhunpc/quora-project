# Generated by Django 2.0.4 on 2018-05-03 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='logid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
