from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
	date=datetime.datetime.now()
	msg='<h1>Hello friend Good evening</h1>'
	msg=msg+'<h1> Now server time is:'+str(date)+'</h1>'
	return HttpResponse(msg)
	
