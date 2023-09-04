from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(title="IceCream", price=30, inventory=2)
        

        self.assertEqual(menu.title, "IceCream")
        self.assertEqual(menu.price, 30)
        self.assertEqual(menu.inventory, 2)