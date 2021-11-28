from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms.models import ModelFormOptions
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(null=True, blank=True, max_length=200)
    profile_pic = models.ImageField(null=True, blank=True)
    
    