from django.test import TestCase

from .models import Meeting, Meeting_Minutes, Event, Resource
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(MeetingTittle='python-learning')
    def test_string(self):
        self.assertEqual(str(self.type), 'python-learning')

    def test_tablename(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')



class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(ResourceName='meeting minutes')
    def test_string(self):
         self.assertEqual(str(self.type), 'meeting minutes')