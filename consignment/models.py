from django.db import models
from django.contrib.auth import get_user_model
from Luqman.utils import unique_ladding_no_generator
from django.db.models.signals import pre_save

User = get_user_model()
# Create your models here.

class ShipmentManager(models.Manager):
	def new_or_get(self, request):
		shipment_id = request.session.get("shipment_id",None)
		qs = Shipment.objects.filter(id=shipment_id)
		if qs.count() == 1:
			new_obj = False
			shipment_obj = qs.first()
			shipment_obj.save()
			if request.user.is_authenticated and shipment_obj.user is None:
				shipment_obj.user = request.user
				shipment_obj.save()
			
		else:
			new_obj = True
			shipment_obj = Shipment.objects.create(author=request.user)
			request.session['shipment_id'] = shipment_obj.id
				
		return shipment_obj

	def new(self, author=None):
		shipment_obj = None
		print(shipment_obj)
		if author is not None:
			if author.is_authenticated:
				shipment_obj = author
				print('Heey')
		print(shipment_obj)
		return self.model.objects.create(author=shipment_obj)

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


	# objects = ShipmentManager()

	def __str__(self):
		return self.shipper

	def get_absolute_url(self):
		return reverse('cargo_list', kwars={'pk':self.pk})


def pre_save_create_ladding_no(sender, instance, *args, **kwargs):
	if not instance.ladding_no:
		instance.ladding_no = unique_ladding_no_generator(instance).upper()

pre_save.connect(pre_save_create_ladding_no, sender=Shipment)
		
	