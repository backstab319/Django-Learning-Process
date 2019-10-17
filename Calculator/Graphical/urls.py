from django.urls import path
from Graphical.views import calGraphic

urlpatterns = [
    path("", calGraphic.index, name="graphical"),
]
