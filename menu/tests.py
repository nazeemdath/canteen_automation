from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from menu.models import Menu  # Import your Menu model if needed

class MenuAPITest(APITestCase):
    def setUp(self):
        self.valid_payload = {
            "name": "Test Item",
            "description": "A sample test item",
            "price": "50.00",
            "is_available": True
        }
        self.invalid_payload = {
            "name": "",
            "description": "Invalid item",
            "price": "-10.00",
            "is_available": True
        }

    def test_add_valid_menu_item(self):
        response = self.client.post('/api/menu/', self.valid_payload, format='json')
        print(response.status_code, response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
