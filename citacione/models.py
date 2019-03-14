from django.db import models
import datetime as dt


class Location(models.Model):
     country=models.CharField(max_length=50)
     city=models.CharField(max_length=50)
     place=models.CharField(max_length=50,default='unkown',null=True)

class Category(models.Model):
     category=models.CharField(max_length=50)

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name= models.CharField(max_length =30)
    description=models.TextField()
    location=models.ForeignKey(Location,null=True)
    category=models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def save_image(self):
         self.save()
    def delete_image(self):
      self.delete()

    @classmethod
    def get_image(cls,id):
     try:
      image=Image.objects.get(id=id)
      return image
     except DoesNotExist:
       return Image.objects.get(id=1)

    @classmethod
    def get_category_images(cls,cat):
      categori=Category.objects.get(category=cat.category)
      images=Image,objects.filter(category=categori)
      return images
    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images



# Create your models here.
