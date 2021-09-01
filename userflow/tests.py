from django.test import SimpleTestCase, TestCase
from django.urls import resolve,reverse
from userflow.views import register_page

# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url= reverse('register/')
        self.assertEquals(resolve(url).func,register_page,msg='This page not register')