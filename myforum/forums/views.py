from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is index.")

def special_2001(request):
	return HttpResponse(f"This is year: 2001 special")

def years(request, year):
	return HttpResponse(f"This is year: {year}")