from django.test import TestCase, Client
from django.urls import reverse

class ExecutorPositionViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dashboard_redirect_view(self):
        response = self.client.get(reverse('dashboard_redirect'))
        self.assertEqual(response.status_code, 302)  # Ожидаем перенаправление

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
