from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    a = "abc"
    b = "xyz"

    return HttpResponse(a + b)
