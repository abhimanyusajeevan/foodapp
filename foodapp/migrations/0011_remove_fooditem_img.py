# Generated by Django 3.0.8 on 2020-08-16 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_auto_20200817_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='img',
        ),
    ]
