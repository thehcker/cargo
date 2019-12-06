from django.db import models
from manifest.models import Manifest
from django.db.models.signals import pre_save, post_save
from Luqman.utils import unique_ref_no_generator

# Create your models here.
class Extra(models.Model):
	manifest = models.OneToOneField(Manifest, on_delete=models.CASCADE)
	file_ref_no = models.CharField(max_length=120, blank=True)
	housebl_no = models.CharField(max_length=120)
	consignee2 = models.CharField(max_length=120)
	quantity = models.IntegerField(default=1)
	vehicle_detail = models.TextField(max_length=200)
	weight = models.DecimalField(decimal_places=2, max_digits=20, default=5.00)
	measurement = models.DecimalField(decimal_places=2, max_digits=20, default=5.00)
	cfs = models.CharField(max_length=120)
	destination = models.CharField(max_length=120)

	def __str__(self):
		return self.consignee2

	def get_absolute_url(self):
		return reverse('extra_detail', kwargs={'pk': self.pk})

	@property
	def ref_no_generator(self):
		file_ref = "MSA"
		new_filename = random.randint(1,1000000)
		return f"{file_ref}{new_filename}"

# def pre_save_create_file_ref_no(sender, instance, *args, **kwargs):
# 	if not instance.ref_no:
# 		instance.ref_no = unique_ref_no_generator(instance)
# pre_save.connect(pre_save_create_file_ref_no, sender=Extra)

def create_extra(sender,instance,**kwargs):
	extra,new = Extra.objects.get_or_create(manifest=instance)
 
post_save.connect(create_extra,sender=Manifest)