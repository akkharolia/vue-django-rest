# Generated by Django 2.2 on 2020-02-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_auto_20200219_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
