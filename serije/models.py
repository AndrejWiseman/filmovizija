from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
# from taggit.managers import TaggableManager



# Create your models here.
class Serije(models.Model):
    title = models.CharField(max_length=120)
    originalni_naziv = models.CharField(max_length=120, null=False, default="")
    slug = models.SlugField(default="", null=False)
    godina = models.CharField(max_length=120, null=False, blank=False, default="")
    # zanr = models.CharField(max_length=120, null=False, blank=False)
    imdb_ocena = models.CharField(max_length=120, null=False, default="")
    description = models.TextField(default="")
    # tags = TaggableManager()
    image = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('serije:serije-detaljno', kwargs={'slug': self.slug})


class Epizoda(models.Model):
    epizode = models.ForeignKey(Serije, on_delete=models.CASCADE)
    epizode_date = models.DateField(auto_now_add=True)
    sezona = models.CharField(max_length=120, null=True, blank=True)
    ep = models.CharField(max_length=120, null=True, blank=True)
    epizode_link = models.CharField(max_length=300)
    epizode_preuzmi = models.CharField(default='', max_length=300)


    def __str__(self):
        return self.ep

#
# class Serije(models.Model):
#     title = models.CharField(max_length=100)
#     # image = models.FileField(upload_to='images/')
#     image = CloudinaryField('image')
