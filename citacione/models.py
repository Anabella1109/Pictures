from django.db import models
import datetime as dt

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name= models.CharField(max_length =30)
    description=models.TextField()


# Create your models here.
