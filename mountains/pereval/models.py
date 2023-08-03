from django.db import models
from .selection import LEVEL, STATUS
from .utils import get_image_path

class Users(models.Model):
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc} {self.phone} {self.email}'


class Coords(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    height = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Images(models.Model):
    data_1 = models.ImageField(max_length=255, upload_to=get_image_path)
    title_1 = models.CharField(max_length=255)
    data_2 = models.ImageField(max_length=255, upload_to=get_image_path)
    title_2 = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title_1} {self.title_2}'


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10, default='new')
    level = models.CharField(choices=LEVEL, max_length=10)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} {self.connect} {self.add_time}' \
               f'{self.user} {self.coords} {self.status} {self.level} {self.images}'

