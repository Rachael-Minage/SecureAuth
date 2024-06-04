from django.test import TestCase
from django.test import TransactionTestCase
from django.db import transaction

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






       