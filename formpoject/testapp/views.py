from django.shortcuts import render
from . import forms

# Create your views here.
def studentregistrationview(request):
	form=forms.studentRegister()
	return render (request,'testapp/register.html',{'form':form})
	pass
