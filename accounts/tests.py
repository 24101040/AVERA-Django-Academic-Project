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