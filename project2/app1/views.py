from django.shortcuts import render
from django.http import HttpResponse
#default and clear in vscode
#changed by devops
#change by github
def fun1(request):
    a = "abc"
    b = "xyz"

    return HttpResponse(a + b)
