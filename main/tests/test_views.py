from django.test import TestCase
from django.urls import reverse

from main import forms


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'Home Page')

    def test_about_page_works(self):
        response = self.client.get(reverse('main:about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, 'About Page')

    def test_contact_us_page_works(self):
        response = self.client.get(reverse('main:contact-us'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')
        self.assertContains(response, 'Contact Us Page')
        self.assertIsInstance(response.context['form'], forms.ContactUsForm)
