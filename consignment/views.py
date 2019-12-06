from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from consignment.form import ShipmentForm
from . models import Shipment
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from decorators import superuser_required


# Create your views here.
@login_required
def cargo(request):
	invoices = Shipment.objects.all()
	template = 'cargo.html' #['cargo.html', 'cargo_list.html']
	return render(request, template, {'invoices': invoices})

class CargoDetailView(DetailView):
	model = Shipment
	context_object_name = 'ship'
	template_name = 'cargo_detail.html'

# def partial_invoice_list(request):
# 	template = 'partial_invoice_list.html'
# 	return render(request, template)

def save_invoiceform(request, form, template_name):
	data = {}
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			data["form_is_valid"] = True
			invoices = Shipment.objects.all()
			data['html_invoice_list'] = render_to_string('partial_invoice_list.html', {'invoices': invoices})
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data["html_form"] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def invoice_create(request):
	if request.method == 'POST':
		form = ShipmentForm(request.POST)
	else:
		form = ShipmentForm()
	return save_invoiceform(request, form, 'partial_invoice_create.html')

def invoice_update(request, pk):
	invoice = get_object_or_404(Shipment, pk=pk)
	if request.method == 'POST':
		form = ShipmentForm(request.POST, instance=invoice)
	else:
		form = ShipmentForm(instance=invoice)
	return save_invoiceform(request, form, 'partial_invoice_update.html')

def invoice_delete(request, pk):
	invoice = get_object_or_404(Shipment, pk=pk)
	data = {}
	if request.method == 'POST':
		invoice.delete()
		data['form_is_valid'] = True
		invoices = Shipment.objects.all()
		data['html_invoice_list'] = render_to_string('partial_invoice_list.html', {'invoices': invoices})
	else:
		context = {'invoice': invoice}
		data['html_form'] = render_to_string('partial_invoice_delete.html', context, request=request)
	return JsonResponse(data)