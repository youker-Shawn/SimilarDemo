from django.test import TestCase

# Create your tests here.
class DemoViewTest(TestCase):
    def test_get_population(self):
        params = {
            "latitude": 40,
            "longitude": 100,
            "radius": 900,
        }
        response = self.client.get('/demo/populations/', data=params)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        resp_data = response.json()
        self.assertIn("result", resp_data)
        self.assertIn("population", resp_data["result"])
        self.assertEqual(resp_data["result"]["population"], 1414948932)  # Mongolia 3170208 + China 1411778724


        