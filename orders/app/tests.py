from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from orders.app.models import User


class AccountTests(APITestCase):
    def test_register_account(self):
        # url = reverse('user-register')
        url = 'user/register'
        data = {'first_name': 'Дмитрий', 'last_name': 'Зайцев', 'email': 'nurgalieva-natalja@yandex.ru',
                'password': 'qwer1234Y', 'company': 'asdadsngfx', 'position': 345347}
        response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
