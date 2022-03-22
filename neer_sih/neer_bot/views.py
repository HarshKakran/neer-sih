from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bot, Trash, LastLocation, Obstacles, LastCollection, GarbageCollectionCenter
from .serializers import BotSerializer, TrashSerializer, LastLocationSerializer, ObstaclesSerializer, \
    LastCollectionSerializer, GarbageCollectionCenterSerializer


class BotListAPIView(APIView):
    def get(self, request):
        qs = Bot.objects.all()
        return Response({'bots': BotSerializer(qs, many=True).data}, status=status.HTTP_200_OK)


class BotStatusAPIView(RetrieveUpdateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            bot = self.get_object()
            return Response(data={'bot_status': BotSerializer(bot).data}, status=status.HTTP_200_OK)

        except Bot.DoesNotExist:
            return Response(data={'bot_status': 'This bot does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Bot.DoesNotExist:
            return Response(data={'bot_status': 'This bot does not exist'}, status=status.HTTP_404_NOT_FOUND)

        s = BotSerializer(instance=instance, data=self.request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data={'bot_status': s.data}, status=status.HTTP_200_OK)
        return Response(data={'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)


class TrashAPIView(APIView):
    def get(self, request, *args, **kwargs):
        date = request.GET.get('date')
        qs = Trash.objects.filter(date_stamp=date)
        if qs:
            return Response({'trash': TrashSerializer(qs, many=True).data})
        else:
            return Response({'message': 'There is no trash collection for this day.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        s = TrashSerializer(data=self.request.data)
        if s.is_valid():
            s.save()
            return Response({'trash': s.data})
        return Response({'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)
