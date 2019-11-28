from django.db import models
from django.contrib.auth.models import User
from Luqman.utils import unique_ladding_no_generator
from django.db.models.signals import pre_save


# Create your models here.

class Shipment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	ladding_no = models.CharField(max_length=100, blank=True)
	shipper = models.CharField(max_length=100)
	consignee1 = models.CharField(max_length=100)
	notify_party = models.CharField(max_length=100)
	ocean_vessel = models.CharField(max_length=100)
	voyage_no = models.CharField(max_length=100)
	pol = models.CharField(max_length=100)
	pod = models.CharField(max_length=100)
	final_destination = models.CharField(max_length=100)
	description = models.TextField(max_length=150)
	gross_weight = models.FloatField(max_length=50)
	measurement = models.FloatField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.shipper

	def get_absolute_url(self):
		return reverse('cargo_list', kwars={'pk':self.pk})


def pre_save_create_ladding_no(sender, instance, *args, **kwargs):
	if not instance.ladding_no:
		instance.ladding_no = unique_ladding_no_generator(instance)

pre_save.connect(pre_save_create_ladding_no, sender=Shipment)
		
	