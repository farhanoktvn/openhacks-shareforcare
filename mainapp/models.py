from django.db import models
from location_field.models.plain import PlainLocationField

class Need(models.Model):
    name = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=280, null=False)
    city = models.CharField(max_length=255, null=False)
    location = PlainLocationField(based_fields=['city'], zoom=6)
    date_created = models.DateTimeField(auto_now_add=True)

class Extra(models.Model):
    name = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=280, null=False)
    city = models.CharField(max_length=255, null=False)
    location = PlainLocationField(based_fields=['city'], zoom=6)
    date_created = models.DateTimeField(auto_now_add=True)
