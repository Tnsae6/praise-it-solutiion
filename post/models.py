from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=500)
    description = models.TextField()
    #image = models.ImageField(upload_to='postimages/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class homeslider(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliderimages/')


# class ContactUSInfo(models.Model):

#     message_name = models.CharField(max_length=200)
#     message_email = models.EmailField(max_length=100)
#     message_phone = models.CharField(max_length=20)
#     message_subject = models.TextField(max_length=200)
#     message = models.TextField()

#     def __str__(self):
#         return self.message_name


class links(models.Model):
    page = models.CharField(max_length=15)
    link = models.TextField()

    def __str__(self):
        return self.page


class Address(models.Model):

    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.address


class icons(models.Model):

    socialmedia = models.TextField()
    icon = models.ImageField()
    link = models.TextField()

    def __str__(self):
        return self.socialmedia


class OurServices(models.Model):

    service = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.service

class AdditionalServices(models.Model):
    
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class MapAddress(models.Model):

    name = models.CharField(max_length=100)
    maps = models.TextField()

    def __str__(self):
        return self.name
