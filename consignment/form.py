from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
	class Meta:
		model = Shipment

		exclude = ['author', 'ladding_no']