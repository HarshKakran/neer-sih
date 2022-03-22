from django.contrib import admin
from .models import Bot, Trash, LastLocation, Obstacles, LastCollection, GarbageCollectionCenter

# Register your models here.
admin.site.register(Bot)
admin.site.register(LastLocation)
admin.site.register(Trash)
admin.site.register(Obstacles)
admin.site.register(LastCollection)
admin.site.register(GarbageCollectionCenter)