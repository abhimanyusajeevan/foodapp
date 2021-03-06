# Generated by Django 3.0.8 on 2020-08-17 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0013_fooditem_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('addressid', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('paying_online', models.BooleanField(default=False)),
                ('pay_status', models.BooleanField(default=False)),
                ('order_delivered', models.BooleanField(default=False)),
                ('order_status', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='indvdl_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('foodid', models.IntegerField()),
                ('price', models.IntegerField()),
                ('orderparent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.order')),
            ],
        ),
    ]
