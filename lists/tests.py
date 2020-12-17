from django.test import TestCase

class HomePageTest(TestCase):

# Create your tests here.
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
