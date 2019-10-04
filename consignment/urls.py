from django.urls import path
from . import views

urlpatterns = [
	path('',views.cargo, name="cargo"),
	path('extra/',views.extra, name="extra"),
	path('hom/',views.hom, name="hom"),
	path('invoice/create/',views.invoice_create, name="invoice_create"),
	path('partial_invoice/list/',views.partial_invoice_list, name="partial_invoice_list"),
]