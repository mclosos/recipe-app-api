from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_user_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'test123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for new user email in normalized"""
        email = "Test@TEST.cOM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests wrong new user email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123test')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@test.io', '234test')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
