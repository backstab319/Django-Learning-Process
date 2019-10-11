from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {"my_temp":"This is a tempate sent over from django."}
    return render(request,"hello_world/hello_world.html",context=my_dict)

# Create your views here.
