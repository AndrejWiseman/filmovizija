from django.db import models

from cloudinary.models import CloudinaryField


# Create your models here.
class Serije(models.Model):
    title = models.CharField(max_length=100)
    # image = models.FileField(upload_to='images/')
    image = CloudinaryField('image')
