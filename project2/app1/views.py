from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("<h1>This is project 1 -> app1 -> fun1</h1>")
