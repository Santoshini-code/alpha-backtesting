from django.db import models


# Create your models here.

class Templates(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)