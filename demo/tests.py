from django.test import TestCase
from django.urls import reverse
from demo.utils import distance_between_2_locations
from demo.models import CountryPopulation

# Create your tests here.
class DemoViewTest(TestCase):
    fixtures = [
        'population.json',
    ]  # data for test

    def setUp(self) -> None:
        self.population_Mongolia = (
            CountryPopulation.objects.filter(name="Mongolia").first().population
        )
        self.population_China = (
            CountryPopulation.objects.filter(name="China").first().population
        )

    def test_get_population_with_json_response(self):
        params = {
            "latitude": 40,
            "longitude": 100,
            "radius": 900,
        }
        response = self.client.get(reverse("demo:population"), data=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        resp_data = response.json()
        self.assertIn("result", resp_data)
        self.assertIn("population", resp_data["result"])
        self.assertIsInstance(resp_data["result"]["population"], int)

    def test_get_population_near_China_and_Mongolia(self):
        params = {
            "latitude": 40,
            "longitude": 100,
            "radius": 900,
        }
        response = self.client.get(reverse("demo:population"), data=params)
        resp_data = response.json()
        self.assertEqual(
            resp_data["result"]["population"],
            self.population_China + self.population_Mongolia,
        )

    def test_get_population_with_missing_parameter(self):
        params_missing = {
            "latitude": 40,
            "longitude": 100,
        }
        response = self.client.get(reverse("demo:population"), data=params_missing)
        resp_data = response.json()
        self.assertEqual(resp_data["code"], 400)
        self.assertIn("missing parameter", resp_data["message"])

    def test_get_population_with_wrong_type_parameter(self):
        params_type_wrong = {
            "latitude": 40,
            "longitude": "abc",
            "radius": 900,
        }
        response = self.client.get(reverse("demo:population"), data=params_type_wrong)
        resp_data = response.json()
        self.assertEqual(resp_data["code"], 400)
        self.assertIn("parameter type wrong", resp_data["message"])

    def test_get_population_with_parameter_out_of_range(self):
        params_latitude_out_of_range = {
            "latitude": 100,
            "longitude": 100,
            "radius": 900,
        }
        resp_data = self.client.get(
            reverse("demo:population"), data=params_latitude_out_of_range
        ).json()
        self.assertEqual(resp_data["code"], 400)
        self.assertIn("parameter out of range", resp_data["message"])

        params_longitude_out_of_range = {
            "latitude": 40,
            "longitude": -200,
            "radius": 900,
        }
        resp_data = self.client.get(
            reverse("demo:population"), data=params_longitude_out_of_range
        ).json()
        self.assertEqual(resp_data["code"], 400)
        self.assertIn("parameter out of range", resp_data["message"])

        params_radius_out_of_range = {
            "latitude": 40,
            "longitude": 100,
            "radius": 10,
        }
        resp_data = self.client.get(
            reverse("demo:population"), data=params_radius_out_of_range
        ).json()
        self.assertEqual(resp_data["code"], 400)
        self.assertIn("parameter out of range", resp_data["message"])


class DemoUtilTest(TestCase):
    def setUp(self) -> None:
        self.Guangzhou = (23.125178, 113.280637)
        self.Beijing = (39.904989, 116.405285)

    def test_get_distance(self):
        distance = distance_between_2_locations(self.Guangzhou, self.Beijing)
        self.assertEqual(distance, 1883.7445935431217)

    def test_get_distance_with_wrong_input(self):
        error_location = ("abc", 113.280637)
        distance = distance_between_2_locations(error_location, self.Beijing)
        self.assertIsNone(distance)

        error_location = 123
        distance = distance_between_2_locations(error_location, self.Beijing)
        self.assertIsNone(distance)
