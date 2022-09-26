from django.db import models
from django.urls import reverse
# Create your models here.
class backgroundimage(models.Model):
    image1 =models.fieldName = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    ()
    logo = models.fieldName = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

class intro(models.Model):
    
    introtext=models.CharField(max_length = 100)
    subtext = models.CharField(max_length = 200)

class main_service(models.Model):

    names = models.CharField(max_length=30)
    redirect = models.CharField(max_length=10)
    explain = models.TextField()
    picture = models.ImageField(null=True, upload_to = 'mainservicesimage/')

    def absolute_url(self):
        return reverse('')
    
class additionalservices(models.Model):

    names = models.CharField(max_length=30)   
    explain = models.TextField()
    picture =models.ImageField(null=True, upload_to = 'additionalservicesimage/')

class Benefit(models.Model):
   
    explain = models.TextField()

class Technologylevel(models.Model):

    explain = models.TextField()

class faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

