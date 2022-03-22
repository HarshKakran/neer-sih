from django.db import models


class Bot(models.Model):
    name =  models.CharField(max_length=200)
    # lastLocation = models.ForeignKey('LastLocation', on_delete=models.)

class Trash(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    date = models.DateField()
    inorganic_trash = models.DecimalField(max_digits=5, decimal_places=2)
    organic_trash = models.DecimalField(max_digits=5, decimal_places=2)

class LastLocation(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    image = models.ImageField(upload_to='geo-locations/')
    time = models.DateTimeField()

class Obstacles(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
