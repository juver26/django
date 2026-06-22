from django.db import models
class User(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20,unique=True)
    description = models.TextField()
    password = models.CharField(max_length=20)
    followers = models.PositiveBigIntegerField(default=0)
    photo = models.ImageField(upload_to="profiles")
# Create your models here.
