from django.contrib import admin
from .models import Shipment

# Register your models here.

class ShipmentAdmin(admin.ModelAdmin):
	class Meta:
		model = Shipment

admin.site.register(Shipment, ShipmentAdmin)
