from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from consignment.form import ShipmentForm
from . models import Shipment

# Create your views here.

def cargo(request):
	shipment = Shipment.objects.all()
	template = 'cargo.html'
	return render(request, template, {'shipment': shipment})

def partial_invoice_list(request):
	template = 'partial_invoice_list.html'
	return render(request, template)

def invoice_create(request):
	data = {}
	if request.method == 'POST':
		form = ShipmentForm(request.POST)
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			invoices = Shipment.objects.all()
			data['html_invoice_list'] = render_to_string('partial_invoice_list.html', {'invoices': invoices})
		else:
			data['form_is_valid'] = False
	else:
		form = ShipmentForm()
	data['html_form'] = render_to_string('partial_invoice.html', {'form': form}, request=request,)
	return JsonResponse(data)

def extra(request):
	context = {}
	template = 'extra.html'
	return render(request, template, context)

def hom(request):
	context = {}
	template = 'hom.html'
	return render(request, template, context)
