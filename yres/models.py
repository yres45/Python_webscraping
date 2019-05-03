from django.db import models
#
class Package (models.Model):
      name = models.CharField(max_length=100)
      track = models.CharField(max_length=100)
      number = models.CharField(max_length=100)
      point = models.CharField(max_length=100)
      
      # Create your models here.
