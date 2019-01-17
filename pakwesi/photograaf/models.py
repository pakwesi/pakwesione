from django.db import models
from django.conf import settings

# Create your models here.
class contact_us(models.Model):
    naam = models.CharField(max_length=120)
    email = models.EmailField()
    onderwerp = models.CharField(max_length=250)
    bericht = models.TextField()

    def __str__(self):
        return self.naam
