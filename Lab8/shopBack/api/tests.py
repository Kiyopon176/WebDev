from django.test import TestCase
from django.db import models

# Create your tests here.
class Person():
    name = models.CharField(max_length=255)
    

