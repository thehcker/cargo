# Generated by Django 2.2.5 on 2019-11-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0004_shipment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='ladding_no',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]