from django.db import models

# Create your models here.


class CountryPopulation(models):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    continent = models.CharField(max_length=2)
