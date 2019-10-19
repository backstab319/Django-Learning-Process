from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class PostGresPage:
    def indexPostGresApp(request):
        return render(request,"PostGresApp/index.html")

    def indexPostGres(request):
        postGresData = {
            "title":"PostGresPage",
            "head1":"Welcome to Postgres Page!",
        }
        return render(request, "PostGres/index.html", context=postGresData)
