from django.urls import path
from ClassAppOne import views

urlpatterns = [
    path("",views.index,name="index"),
    path("url1",views.url1Con,name="url1"),
    path("url2",views.url2Con,name="url2"),
    path("url3",views.url3Con,name="url3"),
    path("url4",views.url4Con,name="url4"),
]