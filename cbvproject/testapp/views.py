from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWorld_view(View):
	def get(self,request):
		return HttpResponse('<h1>This is class based views</h1>')

class HellloWorldTemplate_View(TemplateView):
	template_name="testapp/result.html"

class HellloWorldTemplateContext(TemplateView):
	template_name="testapp/info.html"

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['name']='Durga'
		context['subject']='Python'
		context['mark']=100
		return context