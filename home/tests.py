from django.test import APITestCase
from django.urls import reverse
from products.models import Restaurant

# Create your tests here.
class RestaurantInfoAPITest(APITestCase):
    def setup(self):
        self.restaurant = Restaurant.objects.Create(
            name = "Test Restaurant",
            address = "123 Test St",
            operating_days = "Mon,Tue"
        )

    def test_get_restaurant_info(self):
        response = self.client.get('/api/restaurant-info/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], self.restaurant.name)
        self.assertEqual(response.data[0]['address'], self.restaurant.address)