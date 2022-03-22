from django.db import models
import secrets


class Bot(models.Model):
    BOT_STATUS_STUCK = "stuck"
    BOT_STATUS_WORKING = "working"
    BOT_STATUS_RETURNING = "returning"
    BOT_STATUS_INACTIVE = "inactive"

    BOT_STATUS_CHOICES = [
        (i, i) for i in [BOT_STATUS_STUCK, BOT_STATUS_WORKING, BOT_STATUS_RETURNING, BOT_STATUS_INACTIVE]
    ]

    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=64, null=True, blank=True, choices=BOT_STATUS_CHOICES)
    battery_status = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = secrets.token_hex(5).upper()
        super(Bot, self).save(*args, **kwargs)


class Trash(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    date_stamp = models.DateField(auto_now_add=True, null=True, blank=True)
    degradable_trash = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    non_degradable_trash = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.bot} - Degradable Trash: {self.degradable_trash} kg, Non-Degradable Trash: {self.non_degradable_trash} kg - {self.date_stamp}'


class LastLocation(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    image = models.ImageField(upload_to='geo-locations/', null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.bot} - ({self.lat}, {self.lon}) at {self.time}'


class Obstacles(models.Model):
    OBSTACLE_STATUS_REMOVED = 'removed'
    OBSTACLE_STATUS_FOUND = 'found'

    OBSTACLE_STATUS_CHOICES = [
        (i, i) for i in [OBSTACLE_STATUS_REMOVED, OBSTACLE_STATUS_FOUND]
    ]

    lat = models.DecimalField(max_digits=22, decimal_places=16)
    lon = models.DecimalField(max_digits=22, decimal_places=16)
    status = models.CharField(max_length=64, choices=OBSTACLE_STATUS_CHOICES, null=True, blank=True)
    slug = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'({self.lat}, {self.lon}) - {self.status}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = secrets.token_hex(5).upper()
        super(Obstacles, self).save(*args, **kwargs)



class LastDump(models.Model):
    bot = models.ForeignKey('Bot', on_delete=models.CASCADE)
    date_time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dump_centre = models.ForeignKey('TrashCollectionCenter', on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.date_time_stamp}-{self.dump_centre}-{self.weight} kg'


class TrashCollectionCenter(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state} - {self.pincode}'
