from django.test import TestCase
from django.urls import reverse
from demo.utils import distance_between_2_locations

# Create your tests here.
class DemoViewTest(TestCase):
    fixtures = [
        'population.json',
    ]  # data for test

    def setUp(self) -> None:
        self.population_Mongolia = 3170208
        self.population_China = 1411778724

    def test_get_population(self):
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
        self.assertEqual(
            resp_data["result"]["population"],
            self.population_China + self.population_Mongolia,
        )


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
