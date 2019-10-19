from django.urls import path
from PostGresApp.views import PostGresPage

urlpatterns = [
    path("",PostGresPage.indexPostGresApp,name="index"),
]
