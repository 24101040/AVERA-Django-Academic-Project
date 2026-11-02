from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user,
            phone='01712345678'
        )

        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.user_type, 'supporter')
        self.assertEqual(profile.phone, '01712345678')

    def test_profile_string_representation(self):
        profile = Profile.objects.create(user=self.user)

        self.assertEqual(str(profile), 'testuser')
from django.urls import reverse


class AccountViewTest(TestCase):

    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        User.objects.create_user(
            username='loginuser',
            password='testpassword123'
        )

        response = self.client.post(reverse('login'), {
            'username': 'loginuser',
            'password': 'testpassword123'
        })

        self.assertRedirects(response, reverse('home'))