from django.shortcuts import render
from django.http import HttpResponse
#default and clear in vscode
#changed by devops
def fun1(request):
    a = "abc"
    b = "xyz"

    return HttpResponse(a + b)
