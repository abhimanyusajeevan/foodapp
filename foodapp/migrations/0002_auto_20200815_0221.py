# Generated by Django 3.0.8 on 2020-08-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='regdata',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
