from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    organization_name = models.CharField(max_length=2500, null=True, blank=True)
    location = models.CharField(max_length=2500, null=True, blank=True)
    phone = models.CharField(max_length=2500, null=True, blank=True)
    birthday = models.CharField(max_length=2500, null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    class Meta:
        db_table = 'users'
