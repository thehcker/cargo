from django.contrib import admin
from .models import Manifest

# Register your models here.
class ManifestAdmin(admin.ModelAdmin):
	class Meta:
		model = Manifest

admin.site.register(Manifest, ManifestAdmin)
