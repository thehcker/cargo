from django.contrib import admin
from .models import Extra

# Register your models here.
class Extraadmin(admin.ModelAdmin):
	class Meta:
		model = Extra

admin.site.register(Extra, Extraadmin)