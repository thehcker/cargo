from django.db import models

# Create your models here.

class Shipment(models.Model):
	ladding_no = models.CharField(max_length=100)
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
