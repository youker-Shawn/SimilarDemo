from django.views import View
from django.http import JsonResponse
from similardemo.utils import api_response

# Create your views here.


class PopulationView(View):
    def get(self, request):
        ret_data = api_response(
            result={
                "population": 123,
            }
        )
        return JsonResponse(ret_data)
