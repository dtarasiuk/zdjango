from django.test import TestCase
from models import UserInfo

class ModelTest(TestCase):
    def test_fixtures(self):
        infos_count = UserInfo.objects.count()
        self.assertEqual(infos_count,1)

    def test_mainpage(self):
        response = self.client.get('/simple/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Name:')
