from django.db import models

# Create your models here.
class student(models.Model):
    id = models.
    first_name = models.CharField(maxlength = 100)
    last_name = models.CharField(maxlength = 100)
