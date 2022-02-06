from django.shortcuts import render
import datetime
# Create your views here.
def dateinfo(request):
	date= datetime.datetime.now()
	my_dict={'msg': date}
	return render(request,'testApp/test.html',context = my_dict)
	pass
