# Generated by Django 2.0.4 on 2018-05-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_auto_20180506_0551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('ansid', models.CharField(max_length=50)),
            ],
        ),
    ]