from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Meeting_Minutes, Event, Resource
import datetime
from .forms import MeetingForm





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

#Form tests IS NOT WORKING FOR ME , WILL HAVE TO TRY IT AGIN 

class MeetingType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        data={
            'MeetingTittle':'meeting',
            'MeetingDate':'2021-02-24',
            'Location':'seattle wa',
            'MeetingTime':'13:00:00',
            'Agenda':'meeing agenda'


         }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)