# Generated by Django 2.2.5 on 2019-12-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manifest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_ref_no', models.CharField(blank=True, max_length=120)),
                ('housebl_no', models.CharField(max_length=120)),
                ('consignee2', models.CharField(max_length=120)),
                ('quantity', models.IntegerField(default=1)),
                ('vehicle_detail', models.TextField(max_length=200)),
                ('weight', models.DecimalField(decimal_places=2, default=5.0, max_digits=20)),
                ('measurement', models.DecimalField(decimal_places=2, default=5.0, max_digits=20)),
                ('cfs', models.CharField(max_length=120)),
                ('destination', models.CharField(max_length=120)),
                ('manifest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manifest.Manifest')),
            ],
        ),
    ]
