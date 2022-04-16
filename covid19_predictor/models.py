from tabnanny import verbose
from tokenize import Triple
from django.db import models

class CovidSymptoms(models.Model):
    cough = models.FloatField()
    fever = models.FloatField()
    breath = models.FloatField()
    age = models.IntegerField()
    environment = models.IntegerField()
    hypertension = models.IntegerField()
    diabetes = models.IntegerField()
    cardiovascular = models.IntegerField()
    respiratory = models.IntegerField()
    immune = models.IntegerField()

    class Meta:
        verbose_name_plural = "Covid Symptoms"
    