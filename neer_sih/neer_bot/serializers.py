from rest_framework import serializers
from .models import LastLocation, Bot, Trash, Obstacles, LastDump, TrashCollectionCenter


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


class LastDumpSerializer(serializers.ModelSerializer):
    dump_centre = serializers.PrimaryKeyRelatedField(queryset=TrashCollectionCenter.objects.all())
    bot = serializers.SlugRelatedField(slug_field='slug', queryset=Bot.objects.all())

    class Meta:
        model = LastDump
        fields = ('date_time_stamp', 'dump_centre', 'weight', 'bot')



class TrashCollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCollectionCenter
        fields = ('address', 'city', 'state', 'pincode')
