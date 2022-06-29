from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import User, ConfirmEmailToken


class AccountTests(APITestCase):

    def test_register_account(self):
        count = User.objects.count()
        url = reverse('app:user-register')
        user = {
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test1@test.com',
            'password': 'qwertyuiolp;',
            'company': 'rogaikopyta',
            'position': 'manager',
            'type': 'buyer',
        }
        response = self.client.post(url, user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['Status'], True)
        self.assertEqual(User.objects.count(), count + 1)

    def test_ConfirmAccount(self):
        url = reverse('app:user-register-confirm')
        user = User.objects.create_user(
            first_name='Test',
            last_name='Test',
            email='test@test.com',
            password='qwertyuiolp;',
            company='rogaikopyta',
            position='manager',
            type='buyer',
            is_active=True
        )
        token = ConfirmEmailToken.objects.create(user_id=user.id).key
        data = {'email': user.email, 'token': token}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_AccountDetails(self):
        url = reverse('app:user-details')
        user = User.objects.create_user(
            first_name='Test',
            last_name='Test',
            email='test@test.com',
            password='qwertyuiolp;',
            company='rogaikopyta',
            position='manager',
            type='buyer',
            is_active=True
        )
        token = Token.objects.create(user=user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_AccountDetails(self):
        url = reverse('app:user-details')
        user = User.objects.create_user(
            first_name='Test',
            last_name='Test',
            email='test@test.com',
            password='qwertyuiolp;',
            company='rogaikopyta',
            position='manager',
            type='buyer',
            is_active=True
        )
        token = Token.objects.create(user=user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, {'first_name': 'tseT'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['Status'], True)


class ShopTests(APITestCase):
    def test_product_info(self):
        url = reverse('app:shops')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('Errors', response.data)



