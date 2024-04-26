from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
    )
    address = models.TextField(null=True, blank=True, max_length=1000)
    age = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
