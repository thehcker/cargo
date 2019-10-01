from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cargo(request):
	context = {}
	template = 'cargo.html'
	return render(request, template, context)

def extra(request):
	context = {}
	template = 'extra.html'
	return render(request, template, context)

def hom(request):
	context = {}
	template = 'hom.html'
	return render(request, template, context)
