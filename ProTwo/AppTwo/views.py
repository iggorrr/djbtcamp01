from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    helpdict = {"help_value": "Help Page"}
    return render(request, 'AppTwo/help.html', context=helpdict)

def other(request):
    return HttpResponse("Any other page")
