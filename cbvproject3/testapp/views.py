from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class ComapnyListView(ListView):
	model=Company
class ComapnyDetailView(DetailView):
	model=Company