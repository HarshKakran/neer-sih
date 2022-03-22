from django.contrib import admin
from .models import Bot, LastLocation, Trash

# Register your models here.
admin.site.register(Bot)
admin.site.register(LastLocation)
admin.site.register(Trash)