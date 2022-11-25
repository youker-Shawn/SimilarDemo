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
        radius = request.GET.get("radius")  # kilometers

        # missing parameter
        if not all((latitude, longitude, radius)):
            logging.warning(f"Missing parameter:{latitude} {longitude} {radius}")
            return JsonResponse(api_response(code=400, msg="missing parameter"))

        # parameter type wrong
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            radius = int(radius)
        except Exception as e:
            logging.warning(f"Parameter type wrong:{latitude} {longitude} {radius}")
            return JsonResponse(api_response(code=400, msg="parameter type wrong"))

        # parameter out of range
        is_valid_latitude = True if -90 < latitude < 90 else False
        is_valid_longitude = True if -180 < longitude < 180 else False
        is_valid_radius = (
            True if 100 < radius < 10000 else False
        )  #  counting unit: Kilometers
        if not all((is_valid_latitude, is_valid_longitude, is_valid_radius)):
            logging.warning(f"Parameter out of range:{latitude} {longitude} {radius}")
            return JsonResponse(api_response(code=400, msg="parameter out of range"))

        population_sum = 0
        input_location = (latitude, longitude)
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
