# Generated by Django 3.0.8 on 2020-08-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_auto_20200816_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
