from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello and welcome to index page of AppTwo")

def help(request):
    helpdict = {"help":"This is the help section","info":"This is sent from django template","h1":"This is heading 1",}
    return render(request,"AppTwo/AppTwo.html",context=helpdict)

# Create your views here.
