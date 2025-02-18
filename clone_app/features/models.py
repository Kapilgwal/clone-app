from django.db import models
from django.utils.timezone import now
# Create your models here.


class Posts(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
        
class Followers(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)