from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
a,b = 5,3
def index(request): 
    return HttpResponse("a= 5,b= 3")
def url1Con(request):
    res = "a + b = ",a+b
    return HttpResponse(res)
def url2Con(request):
    res = "a - b = ",a-b
    return HttpResponse(res)
def url3Con(request):
    res = "a * b = ",a*b
    return HttpResponse(res)
def url4Con(request):
    res = "a / b = ",a/b
    return HttpResponse(res)

def index_two(request):
    page_dict = {
        "date":datetime.date,
        "time":datetime.datetime._local_timezone,
        "head1":"Welcome to nascar page!",
        "jeff":"Jeffery Michael Gordon is an American former professional stock car racing driver, currently an announcer for Fox NASCAR, and a top executive for Hendrick Motorsports.",
        "head2":"Legendary Drivers",
    }
    return render(request,"ClassAppOne/index.html",context=page_dict)