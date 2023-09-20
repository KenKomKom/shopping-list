# Create your tests here.
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 302)

    def test_main_using_main_template(self):
        response = Client().get('')
        print(response)
        self.assertTemplateUsed(response, 'login.html')