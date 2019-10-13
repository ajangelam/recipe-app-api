from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Super user (forced login)
        email = "admin@londonappdev.com"
        password = "Password123"
        self.admin_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.client.force_login(self.admin_user)

        # Normal user
        email = "test@londonappdev.com"
        password = "Password123"
        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name='User1 Test'
        )

    def test_users_listed(self):
        """
        Tests that users are listed on the user page.
        """
        # Generate url for admin user list page
        url = reverse('admin:core_user_changelist')

        # Perform http get for url
        response = self.client.get(url)

        # Check if response contains items
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """
        Tests that the user edit page works.
        """
        # Generate url /admin/core/user/<id>
        url = reverse('admin:core_user_change', args=[self.user.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
