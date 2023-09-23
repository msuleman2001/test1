from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_fun(request):
    return HttpResponse("I am in app 2 method 1")

def app2_fun2(request):
    return HttpResponse("I am in app 2 method 2")
