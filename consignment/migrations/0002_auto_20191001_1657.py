# Generated by Django 2.2.5 on 2019-10-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
