from django.test import TestCase
from .models import Image,Category,Location

class ImageTestClass(TestCase):
       def setUp(self):
          self.cat=Category(category='food')
          self.location=Location(country='Rwanda',city='Kigali',place="Raddison blue")
          self.image=Image(image='@heroo',name='koko',description="koko koko koko okruuuuuu",location=self.location,category=self.cat)

      #  def tearDown(self):
      #      Category.objects.all().delete()
      #      Location.objects.all().delete()
      #      Image.objects.all().delete()
        
       def test_instance(self):
           self.assertTrue(isinstance(self.image, Image))

       def test_save_method(self):
          self.cat.save()
          self.location.save()
          self.image.save_image()
          images = Image.objects.all()
          self.assertTrue(len(images) > 0)

       def test_delete_method(self):
         self.cat.save()
         self.location.save()
         self.image.save_image()
         self.image.delete_image()
         images = Image.objects.all()
         self.assertTrue(len(images) == 0)

       def test_get_image_by_id(self):
         image1 = Image.get_image(id=self.image.id)
         self.assertEqual(self.image, image1)

       def test_get_images_by_category(self):
          images=Image.get_category_images(cat=self.cat)
          
          self.assertTrue(len(images>0))
          

      
  

# Create your tests here.
