from django.shortcuts import render
from django.http import HttpResponse
# change in vs code
#change on git
#change after add az url
# Create your views here.
def fun1(request):
    a = "abc"
    b = "xyz"

    return HttpResponse(a + b)
