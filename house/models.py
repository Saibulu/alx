from django.db import models
# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Company(models.Model):
    client = models.CharField(max_length=50)
    project = models.IntegerField()
    hours_of_support = models.IntegerField()
    workers = models.IntegerField()

    def __str__(self):
        return self.client

class Teams(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.title




class Slider(models.Model):
    slider_head = models.CharField(max_length=50)
    slider_description = models.CharField(max_length=50)
    slider_btn = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.slider_head

class Teams(models.Model):
   name = models.CharField(max_length=50)
   desc= models.CharField(max_length=50)
   img = models.ImageField(upload_to='Teams/')

   def __str__(self):
       return self.name

class pricings(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.product


