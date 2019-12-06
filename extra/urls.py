from django.urls import path
from django.conf.urls import url
from extra import views

urlpatterns = [
	path('extra/',views.extra, name="extra"),
	path('extra/<int:pk>/',views.ExtraDetailView.as_view(), name="extra_detail"),
	path('extra/create/',views.create_extra, name="extra_create"),
	url(r'^extra/(?P<pk>[0-9]+)/update/$',views.update_extra, name="extra_update"),
	url(r'^extra/(?P<pk>[0-9]+)/delete/$',views.delete_extra, name="extra_delete"),
]