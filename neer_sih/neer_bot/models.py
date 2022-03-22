from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=200)
    # lastLocation = models.ForeignKey('LastLocation', on_delete=models.)


class Trash(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    date = models.DateField()
    inorganic_trash = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    organic_trash = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class LastLocation(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    image = models.ImageField(upload_to='geo-locations/', null=True, blank=True)
    time = models.DateTimeField()


class Obstacles(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    lon = models.DecimalField(max_digits=22, decimal_places=16)
