from django.db import models
import datetime as dt


class Location(models.Model):
     country=models.CharField(max_length=50)
     city=models.CharField(max_length=50)

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name= models.CharField(max_length =30)
    description=models.TextField()
    location=models.ForeignKey(Location)



# Create your models here.
