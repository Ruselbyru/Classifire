from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse
from .views import viewimg

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_viewimg_url_is_resolved(self):
        url= reverse('image',args=['1'])
        self.assertEquals(resolve(url).func,viewimg)
