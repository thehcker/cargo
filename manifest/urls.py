from django.urls import path
from django.conf.urls import url
from manifest import views

urlpatterns = [
	path('hom/', views.manifest, name='hom'),
	path('hom/<pk>/', views.ManifestDetailView.as_view(), name='hom_detail'),
	path('hom/create/', views.create_hom, name='hom_create'),
	url(r'^hom/(?P<pk>[0-9]+)/update/$', views.update_hom, name='hom_update'),
	url(r'^hom/(?P<pk>[0-9]+)/delete/$', views.delete_hom, name='hom_delete'),
]