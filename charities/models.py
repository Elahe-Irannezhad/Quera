from django.db import models
from accounts.models import User

EXPERIENCE_CHOICES = (
    (0, 'Beginner'),
    (1, 'Intermediate'),
    (2, 'Expert')
)

GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
)

STATE_CHOICES = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done"),
)

class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    state = models.CharField(choices=STATE_CHOICES, default='P', max_length=20)
    title = models.CharField(max_length=60)