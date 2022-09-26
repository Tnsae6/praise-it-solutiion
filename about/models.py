from django.db import models

# Create your models here.
class mission(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class vision(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()

    def __str__(self):
        return self.title

class values(models.Model):
    title = models.CharField(max_length =  20)
    description =models.TextField()

    def __str__(self):
        return self.title   

class welcome(models.Model):
    title = models.CharField(max_length=100, blank = True)             
    passage = models.TextField()

    def __str__(self):
        return self.title

class experts(models.Model):
    name = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30)
    photo = models.ImageField()

    def __str__(self):
        return self.name


