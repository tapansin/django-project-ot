from ast import Return
from urllib import request
from defer import return_value
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_view(request):
    print('this line printed by view fuction while processing request')
    print(10/0)
    return HttpResponse ('<h1>this is custom middleware</h1>')