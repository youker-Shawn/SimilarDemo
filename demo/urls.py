from django.urls import path
from demo.views import PopulationView

urlpatterns = [
    path('populations/', PopulationView.as_view(), name="population"),
]
