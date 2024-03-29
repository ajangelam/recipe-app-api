from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful.
        """
        email = "test@londonappdev.com"
        password = "Password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized (char cases).
        """
        email = 'test@LONDONAPPDEV.COM'
        password = "Password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error.
        """
        with self.assertRaises(ValueError):
            email = None
            password = "Password123"
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_new_superuser(self):
        """
        Test creating a new superuser.
        """
        email = "test@londonappdev.com"
        password = "Password123"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        # user.is_superuser is part of PermissionsMixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
