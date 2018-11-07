from django.test import TestCase
from django.test.client import *
from django.shortcuts import reverse

# Create your tests here.
client = Client()
response1 = client.post(reverse('create_course'), {'course_number':'001', 'course_name':'math', 'instructor':'Mike'})
response2 = client.post(reverse('create_student'), {'andrew_id':'lyulianl', 'first_name':'Lyuliang', 'last_name':'Liu'})
