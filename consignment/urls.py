from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.cargo, name="cargo"),
	path('cargo_detail/<int:pk>',views.CargoDetailView.as_view(), name="cargo_detail"),
	path('invoice/create/',views.invoice_create, name="invoice_create"),
	# path('partial_invoice/list/',views.partial_invoice_list, name="partial_invoice_list"),
	url(r'^invoice/(?P<pk>[0-9]+)/update/$',views.invoice_update, name="invoice_update"),
	url(r'^invoice/(?P<pk>[0-9]+)/delete/$',views.invoice_delete, name="invoice_delete"),
]