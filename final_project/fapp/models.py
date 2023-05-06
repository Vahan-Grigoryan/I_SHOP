from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=150, unique=True)
    last_name = models.CharField(verbose_name="last name", max_length=150, unique=True)
    tel = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    post_code = models.IntegerField()
