from django.db import models

# Create your models here.

class set(models.Model):
    Type = models.CharField(max_length=20)
    image1= models.ImageField(upload_to='setImages', width_field=800,height_field=600)
    price1 = models.CharField(max_length=20)
    # image2= models.ImageField(null=True)
    # price2 = models.CharField(null=True, max_length = 20)
    # image3= models.ImageField(null=True)
    # price3 = models.CharField(null=True, max_length=20)
    # image4= models.ImageField(null=True)
    # price4 = models.CharField(null=True, max_length=20)
    # image5= models.ImageField(null=True)
    # price5 = models.CharField(null=True, max_length=20)
    # image6= models.ImageField(null=True)
    # price6 = models.CharField(null=True, max_length=20)

class single(models.Model):
    image = models.ImageField(upload_to='singleimages')
    price = models.CharField(max_length=20)


class Items(models.Model):
    name = models.CharField(max_length=50)
    Price = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='Items', width_field=800, height_field=600)

    def __str__(self):
        return self.name
