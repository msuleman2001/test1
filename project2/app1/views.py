from django.shortcuts import render
from django.http import HttpResponse
#default and clear in vscode
#changed by devops
#change by github
#chnages by ibrahim on devops
# again open the files and made changes in local
def fun1(request):
    a = "abc"
    b = "xyz"

    return HttpResponse(a + b)
