from django.contrib import admin
from .models import Bot, Trash, LastLocation, Obstacles, LastDump, TrashCollectionCenter

# Register your models here.
admin.site.register(Bot)
admin.site.register(LastLocation)
admin.site.register(Trash)
admin.site.register(Obstacles)
admin.site.register(LastDump)
admin.site.register(TrashCollectionCenter)