import logging
from django.views import View
from django.http import JsonResponse
from demo.models import CountryPopulation
from demo.utils import distance_between_2_locations
from similardemo.utils import api_response

# Create your views here.


class PopulationView(View):
    def get(self, request):
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        radius = request.GET.get("radius")

        input_location = (float(latitude), float(longitude))
        radius = int(radius)

        population_sum = 0
        locations = CountryPopulation.objects.all()
        for location in locations:
            iter_locaation = (location.latitude, location.longitude)
            dist = distance_between_2_locations(input_location, iter_locaation)
            if dist and dist < radius:
                logging.debug(f"name:{location.name}, population:{location.population}")
                population_sum += location.population

        ret_data = api_response(
            result={
                "population": population_sum,
            }
        )
        return JsonResponse(ret_data)
