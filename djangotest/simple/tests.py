from django.test import TestCase
from models import UserInfo
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ModelTest(TestCase):
    def test_fixtures(self):
        infos_count = UserInfo.objects.count()
        self.assertEqual(infos_count,1)

    def test_users(self):
        User.objects.create_user(username="zimyand", email='zimyand@gmail.com', password="123123z")
        user = authenticate(username="zimyand", password="123123z")
        if user is None:
            self.fail()
