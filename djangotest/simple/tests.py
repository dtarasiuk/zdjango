from django.test import TestCase
from models import UserInfo, Counter
from django.contrib.auth.models import User
from django.template import Template, Context
import sys
from django.core.management import call_command
from django.contrib.admin.models import LogEntry

class ModelTest(TestCase):
    def test_fixtures(self):
        infos_count = UserInfo.objects.count()
        self.assertEqual(infos_count,1)

    def test_mainpage(self):
        response = self.client.get('/simple/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Name:')

    def test_correct_auth(self):
        user = "zimyand"
        password = "123123z"
        email = 'zimyand@gmail.com'
        User.objects.create_user(username=user, email=email, password=password)
        post_data = {
            'username': user,
            'userpass': password,
        }
        response = self.client.post('/simple/', post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello,")

    def test_incorrect_auth(self):
        post_data = {
            'username': 'incorrectuser',
            'userpass': 'incorrectpass',
        }
        response = self.client.post('/simple/', post_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Hello,")

    def test_middleware(self):
        response = self.client.get('/simple/')
        last_counter = Counter.objects.get()
        self.assertEqual('/simple/', last_counter.url)

    def test_context_processor(self):
        response = self.client.get('/simple/')
        contexts = response.context

        exist = 0
        for item in contexts:
            if item.has_key('settings'):
                settings = item['settings']
                if hasattr(settings,'INSTALLED_APPS'):
                    exist = 1

        self.assertEqual(exist, 1)

    def test_error_edit(self):
        """not full data test"""
        response = self.client.post('/simple/', {'name':'test name'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

    def test_success_edit(self):
        info = UserInfo.objects.get()

        response = self.client.post('/simple/', {'name':'new name', 'surname':'new surname', 'about': 'new about', 'contacts': 'new contacts', 'birthday': '2010-02-17'})
        info = UserInfo.objects.get()
        self.assertEqual([info.name, info.surname, info.about, info.contacts], ['new '+x for x in ['name', 'surname', 'about', 'contacts']])

    def test_calendar_exist(self):
        response = self.client.get('/simple/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, '<select name="birthday_month" id="id_birthday_month">')

    def test_inverted(self):
        """Check if inverted form"""
        response = self.client.get('/simple/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Name:')
        self.assertContains(response, 'Contacts:')
        content = str(response)
        assert(content.find('id="id_name"')>=content.find('id="id_contacts"'))

    def test_tags(self):
        response = self.client.get('/simple/')
        userinfo = UserInfo.objects.get()

        rendered = Template('{% load tagediturl %}{% edit_url "userinfo" %}')
        context = Context({"userinfo": userinfo})
        geturl = rendered.render(context)
        
        url = "/admin/simple/userinfo/%s/" % (userinfo.id)
        
        self.assertEqual(geturl, url, "admin url tag error")
        
        response = self.client.get(geturl)
        self.assertEqual(response.status_code, 200, 'Error in link address to admin: %s')

    def test_command(self):
        std_old = sys.stdin, sys.stdout
        sys.stdout = open("out.txt","r+w")
        call_command('printmodels')
        try:
            response = sys.stdout.readlines()
        finally:
            sys.stdout.close()
            sys.stdin, sys.stdout = std_old
        self.assertFalse(response)

    def test_signals(self):
        old_count = LogEntry.objects.count()
        userobject = UserInfo(name = 'testname', surname = 'testsurname', birthday = '2010-02-17', about = 'test', contacts = 'test');
        userobject.save()
        self.assertNotEqual(old_count, LogEntry.objects.count())
