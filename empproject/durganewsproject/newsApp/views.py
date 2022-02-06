from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'newsapp/index.html')
	
def moviesinfo(request):
	return render(request,'newsapp/index.html')

def danceinfo(request):
	return render(request,'newsapp/index.html')
