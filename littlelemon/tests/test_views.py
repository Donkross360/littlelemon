from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=25, inventory=3)
        Menu.objects.create(title="CranBerry", price=15, inventory=25)
        Menu.objects.create(title="Capaccino", price=20, inventory=30)

    def test_getall(self):
        client = APIClient()

        response = client.get('restaurant/menu/')

        self.assertEqual(response.status_code, 200)

        menu_object = Menu.objects.all()
        serializer = MenuSerializer(menu_object, Many=True)
        self.assertEqual(response.data, serializer.data)
