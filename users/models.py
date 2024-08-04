from django.db import models

from django.db import models
class register(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    mobile_no = models.IntegerField(max_length=255)
    