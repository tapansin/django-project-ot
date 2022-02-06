from django.shortcuts import render
from testapp import forms

# Create your views here.
def student_view(request):
	form= forms.StudentForm()
	return render(request,'testapp/register.html',{'form':form})
