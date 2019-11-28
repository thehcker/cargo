from django import forms
from .models import Extra

class ExtraForm(forms.ModelForm):
	class Meta:
		model = Extra
		fields = '__all__'