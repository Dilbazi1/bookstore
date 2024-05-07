# from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest import TestCase
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

class CustomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='s',
            email='s@bk.ru',
            password='2021'
        )
        self.assertEqual(user.username,'s')
        self.assertEqual(user.email,'s@bk.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='dil',
            email='dil@bk.ru',
            password='2021'
        ) 
        self.assertEqual(admin_user.username,'dil')
        self.assertEqual(admin_user.email,'dil@bk.ru') 
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        

