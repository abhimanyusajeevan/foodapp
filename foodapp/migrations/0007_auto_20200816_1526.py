# Generated by Django 3.0.8 on 2020-08-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_fooditem_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
