from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from .helpers import get_attrs_from_img
from django.conf import settings


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)


class Photo(models.Model):
    title = models.CharField(max_length=1000)
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if self.url and not self.image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.url).read())
            img_temp.flush()
            file_name = self.url.split('/')[-1]
            self.image.save(f"{file_name}", File(img_temp), save=False)

            attrs = get_attrs_from_img(img_temp)
            self.width = attrs['width']
            self.height = attrs['height']
            self.color = attrs['color']
        if self.image and not self.url:
            attrs = get_attrs_from_img(self.image)
            self.width = attrs['width']
            self.height = attrs['height']
            self.color = attrs['color']
        return super(Photo, self).save(*args, **kwargs)
