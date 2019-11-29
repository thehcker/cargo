from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import ManifestForm
from .models import Manifest

# Create your views here.
@login_required
def manifest(request):
	manifests = Manifest.objects.all()
	context = {'manifests': manifests}
	template = 'manifest.html'
	return render(request, template, context)

class ManifestDetailView(DetailView):
	model = Manifest
	context_object_name = 'manifest'
	template_name = 'manifest_detail.html'

def save_extra(request, form, template_name):
	data = {}
	if request.method == "POST":
		if form.is_valid():
			form.save()
			data["form_is_valid"] = True
			manifests = Manifest.objects.all()
			data['html_invoice_list'] = render_to_string("partial_hom_list.html", {"manifests": manifests})
		else:
			data["form_is_valid"] = False
	context = {"form": form}
	data["html_form"] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def create_hom(request):
	if request.method == "POST":
		form = ManifestForm(request.POST)
	else:
		form = ManifestForm()
	return save_extra(request, form, "partial_hom_create.html")

def update_hom(request, pk):
	manifest = get_object_or_404(Manifest, pk=pk)
	if request.method == "POST":
		form = ManifestForm(request.POST, instance=manifest)
	else:
		form = ManifestForm(instance=manifest)
	return save_extra(request, form, "partial_hom_update.html")



def delete_hom(request, pk):
	manifest = get_object_or_404(Manifest, pk=pk)
	data = {}
	if request.method == "POST":
		manifest.delete()
		data["form_is_valid"] = True
		manifests = Manifest.objects.all()
		data["html_invoice_list"] = render_to_string("partial_hom_list.html", {"manifests": manifests})
	else:
		context = {"manifest": manifest}
		data["html_form"] = render_to_string("partial_hom_delete.html", context, request=request)
	return JsonResponse(data)