from django.urls import path
from . import views

urlpatterns = [
	path('',views.cargo, name="cargo"),
	path('extra/',views.extra, name="extra"),
	path('hom/',views.hom, name="hom"),
]