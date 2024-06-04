from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

