from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	s='<h1>Hello welcome to djago classes love you too</h1>'
	return HttpResponse(s)
	
