from django.test import TestCase, Client
from main.models import Product
from django.urls import reverse

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_model_creation(self):
        my_instance = Product.objects.create(name="Test", amount="2", description = "this_is_a_test")
        self.assertEqual(my_instance.name, "Test")
    
    def test_show_main_view(self):
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
