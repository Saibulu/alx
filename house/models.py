from django.db import models


# Create your models here.

class Company(models.Model):
    client = models.IntegerField()
    project = models.IntegerField()
    hoursofsupport = models.IntegerField()
    workers = models.IntegerField()


