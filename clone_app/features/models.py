from django.db import models

# Create your models here.


class Posts(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=1000)
    image = models.ImageField()
    
class Following(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)\
        
class Followers(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)