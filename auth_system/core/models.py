from django.db import models

# Create your models here.
class World(models.Model):
    people = models.IntegerField()
    
