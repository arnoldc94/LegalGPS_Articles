from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(null=True, blank=True, max_length=200)
    profile_pic = models.ImageField(null=True, blank=True, default="profile Pic")
    buisness = models.CharField(max_length=200, default='your buisness name goes here')
    goal = models.CharField(max_length=350, default='Your goal goes here')
    bio = models.TextField(default='Your Bio Goes Here')


