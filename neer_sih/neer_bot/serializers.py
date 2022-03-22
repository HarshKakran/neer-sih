from rest_framework import serializers
from .models import LastLocation, Bot, Trash, Obstacles, LastCollection, GarbageCollectionCenter


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('name', 'status', 'battery_status', 'slug')


class LastLocationSerializer(serializers.ModelSerializer):
    bot = serializers.SlugRelatedField(slug_field='slug', queryset=Bot.objects.all())

    class Meta:
        model = LastLocation
        fields = ('bot', 'lat', 'lon', 'image', 'time_stamp')


class TrashSerializer(serializers.ModelSerializer):
    bot = serializers.SlugRelatedField(slug_field='slug', queryset=Bot.objects.all())

    class Meta:
        model = Trash
        fields = ('bot', 'degradable_trash', 'non_degradable_trash', 'date_stamp')


class ObstaclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacles
        fields = ('lat', 'lon', 'status', 'slug')


class LastCollectionSerializer(serializers.ModelSerializer):
    dump_centre = serializers.SerializerMethodField()

    class Meta:
        model = LastCollection
        fields = ('date_time_stamp', 'dump_centre', 'weight')

    def get_dump_centre(self, obj: LastCollection):
        return obj.dump_centre


class GarbageCollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageCollectionCenter
        fields = ('address', 'city', 'state', 'pincode')
