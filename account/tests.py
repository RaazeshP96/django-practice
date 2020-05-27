from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomTest(TestCase):
    pass


class SignupTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)