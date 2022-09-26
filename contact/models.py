from django.db import models

# Create your models here.

class ContactUSInfo(models.Model):
    
    message_name = models.CharField(max_length=200)
    message_email = models.EmailField(max_length=100)
    message_phone = models.CharField(max_length=20)
    message_subject = models.TextField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.message_name

class MapAddress(models.Model):
    
    name = models.CharField(max_length=100)
    maps = models.TextField()

    def __str__(self):
        return self.name


class icons(models.Model):
    
    socialmedia = models.TextField()
    icon = models.ImageField()
    link = models.TextField()

    def __str__(self):
        return self.socialmedia


class Address(models.Model):
    
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.address