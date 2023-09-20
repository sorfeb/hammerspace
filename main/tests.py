from django.test import TestCase, Client
from main.models import Item
from django.urls import reverse

class mainTest(TestCase):
    def test_main_url_is_exist(self): #checks if /main/ exists
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self): #checks /main/ with main.html template
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_model_creation(self): #Creates an instance of Product with test attributes
        my_instance = Item.objects.create(name="Test", amount="2", description = "this_is_a_test")
        self.assertEqual(my_instance.name, "Test")
    

    def test_show_main_view(self): #tests if main:show_main is functioning correctly
        response = self.client.get(reverse('main:show_main')) #simulate GET request to URL
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'main.html') #verifies that response uses main.html