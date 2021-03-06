# Generated by Django 2.2.5 on 2019-12-06 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ladding_no', models.CharField(blank=True, max_length=100)),
                ('shipper', models.CharField(max_length=100)),
                ('consignee1', models.CharField(max_length=100)),
                ('notify_party', models.CharField(max_length=100)),
                ('ocean_vessel', models.CharField(max_length=100)),
                ('voyage_no', models.CharField(max_length=100)),
                ('pol', models.CharField(max_length=100)),
                ('pod', models.CharField(max_length=100)),
                ('final_destination', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('gross_weight', models.FloatField(max_length=50)),
                ('measurement', models.FloatField(blank=True, max_length=50, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
