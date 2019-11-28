import random
from django.shortcuts import reverse
from django.db import models
from consignment.models import Shipment
from django.db.models.signals import pre_save
from Luqman.utils import unique_ref_no_generator

# Create your models here.
class Manifest(models.Model):
	shipper = models.OneToOneField(Shipment, on_delete=models.CASCADE)
	ref_no = models.CharField(max_length=100, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	shipper_name = models.CharField(max_length=100)
	shipper_address = models.CharField(max_length=100)
	shipper_city = models.CharField(max_length=100)
	shipper_country = models.CharField(max_length=100)
	shipper_tel = models.CharField(max_length=100)
	shipper_email = models.CharField(max_length=100)
	vessel_name = models.CharField(max_length=100)
	voyage_no = models.CharField(max_length=100)
	port_of_loading = models.CharField(max_length=100)
	cfs = models.CharField(max_length=100)

	def __str__(self):
		return self.shipper_name

	def get_absolute_url(self):
		return reverse('hom_detail', kwargs={'pk': self.pk})

	
	def ref_no_generator(self):
		file_ref = "MSA"
		new_filename = random.randint(1,1000000)
		return f"{file_ref}{new_filename}"

def pre_save_create_ref_no(sender, instance, *args, **kwargs):
	if not instance.ref_no:
		instance.ref_no = unique_ref_no_generator(instance)
pre_save.connect(pre_save_create_ref_no, sender=Manifest)

