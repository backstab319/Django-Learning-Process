from django.urls import path
from django.conf.urls import url
from hello_world import views

urlpatterns = [
    path('',views.index,name='index'),
]
