from django.db import models


class Bot(models.Model):
    BOT_STATUS_STUCK = "stuck"
    BOT_STATUS_WORKING = "working"
    BOT_STATUS_RETURNING = "returning"
    BOT_STATUS_INACTIVE = "inactive"

    BOT_STATUS_CHOICES = [
        (i, i) for i in [BOT_STATUS_STUCK, BOT_STATUS_WORKING, BOT_STATUS_RETURNING, BOT_STATUS_INACTIVE]
    ]

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=64, null=True, blank=True, choices=BOT_STATUS_CHOICES)


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

class LastCollection(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('GarbageCollectionCenter', on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class GarbageCollectionCenter(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)
