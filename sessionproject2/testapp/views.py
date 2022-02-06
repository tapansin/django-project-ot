from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,GFForm

# Create your views here.

def name_view(request):
	Form=NameForm()
	return render(request,'testapp/name.html',{'Form':Form})

def age_view(request):
	#name=request.GET('name')
	request.session['name']=name
	Form =AgeForm()
	return render(request,'testapp/age.html',{'Form':Form})
