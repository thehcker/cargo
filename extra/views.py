from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import DetailView
from django.template.loader import render_to_string
from .models import Extra
from .forms import ExtraForm

# Create your views here.
def extra(request):
	extras = Extra.objects.all()
	context = {'extras': extras}
	template = 'extra.html'
	return render(request, template, context)

class ExtraDetailView(DetailView):
	model = Extra
	template_name = 'extra_detail.html'
	context_object_name = 'extra'

def save_extra(request, form, template_name):
	data = {}
	if request.method == "POST":
		if form.is_valid():
			form.save()
			data["form_is_valid"] = True
			extras = Extra.objects.all()
			data['html_invoice_list'] = render_to_string("partial_extra_list.html", {"extras": extras})
		else:
			data["form_is_valid"] = False
	context = {"form": form}
	data["html_form"] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def create_extra(request):
	if request.method == "POST":
		form = ExtraForm(request.POST)
	else:
		form = ExtraForm()
	return save_extra(request, form, "partial_extra_create.html")

def update_extra(request, pk):
	extra = get_object_or_404(Extra, pk=pk)
	if request.method == "POST":
		form = ExtraForm(request.POST, instance=extra)
	else:
		form = ExtraForm(instance=extra)
	return save_extra(request, form, "partial_extra_update.html")

def delete_extra(request, pk):
	extra = get_object_or_404(Extra, pk=pk)
	data = {}
	if request.method == "POST":
		extra.delete()
		data["form_is_valid"] = True
		extras = Extra.objects.all()
		data["html_invoice_list"] = render_to_string("partial_extra_list.html", {"extras": extras})
	else:
		context = {"extra": extra}
		data["html_form"] = render_to_string("partial_extra_delete.html", context, request=request)
	return JsonResponse(data)		