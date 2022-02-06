from typing_extensions import Self
from urllib import response

from django.http import HttpResponse


class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        print('this line printed at pre-processing of request')
        response = self.get_response(request)
        print('this line printed at post-processing of request')
        return response

class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        return HttpResponse('<h1>Currently server is under maintenance</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        s='<h1> Currently we are facing some techinical problems</h1>'
        return HttpResponse(s)

