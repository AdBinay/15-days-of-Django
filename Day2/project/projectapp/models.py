from django.db import models

# Create your models here.
class Person(models.model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)