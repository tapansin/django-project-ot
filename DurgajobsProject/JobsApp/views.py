from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
	s='<h1>Getting hyderbad jobs information </h1>'
	return HttpResponse(s)

def punejobs(request):
	s='<h1>Getting pune jobs information </h1>'
	return HttpResponse(s)
def mumbaijobs(request):
	s='<h1>Getting mumbai jobs information </h1>'
	return HttpResponse(s)
def kolkatajobs(request):
	s='<h1>Getting kolkata jobs information </h1>'
	return HttpResponse(s)
