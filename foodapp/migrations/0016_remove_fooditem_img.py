# Generated by Django 3.0.8 on 2020-08-17 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0015_order_order_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='img',
        ),
    ]