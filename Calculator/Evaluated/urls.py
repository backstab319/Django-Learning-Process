from django.urls import path
from Evaluated.views import EvaluatedCalculator

urlpatterns = [
    path('',EvaluatedCalculator.index, name="evaluated"),
]
