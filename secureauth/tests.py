from django.test import TestCase
from .models import User, Role
from rest_framework.test import APIClient
from rest_framework import status


class UserModelTests(TestCase):

    def test_create_user(self):
        """Test creating a new user with a role."""
        role = Role.objects.create(name='Student')
        user = User.objects.create_user(username='testuser', password='testpassword', role=role)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, role)

    def test_create_role(self):
        """Test creating a new role."""
        role = Role.objects.create(name='Parent')
        self.assertEqual(role.name, 'Parent')
        self.assertTrue(Role.objects.filter(name='Parent').exists())


class UserLoginAPIViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(name='admin')
        self.user = User.objects.create_user(
            username='testuser1',
            password='strongestpassword',
            role=self.role,
        )

   
    def test_login_invalid_credentials(self):
        """Test failed login with invalid credentials."""
        data = {
            'username': 'testuser1',
            'password': 'wrongpassword'
        }
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)  


