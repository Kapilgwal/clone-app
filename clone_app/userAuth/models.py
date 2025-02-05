from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name