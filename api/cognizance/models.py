from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')