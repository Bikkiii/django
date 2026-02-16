from django.db import models
from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # phone = models.CharField(max_length=15)
# Create your models here.
