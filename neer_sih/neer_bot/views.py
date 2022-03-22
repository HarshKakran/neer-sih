from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bot, Trash, LastLocation, Obstacles, LastDump, TrashCollectionCenter
from .serializers import BotSerializer, TrashSerializer, LastLocationSerializer, ObstaclesSerializer, \
    LastDumpSerializer, TrashCollectionCenterSerializer


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


class LastLocationAPIView(APIView):
    def post(self, request):
        s = LastLocationSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'last_location': s.data})
        return Response({'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        bot_slug = request.data.get('bot', '')
        qs = LastLocation.objects.select_related('bot').filter(bot__slug=bot_slug).order_by('-id').first()
        if qs:
            return Response({'last_location': LastLocationSerializer(qs).data})
        return Response({'message': 'Not enough data'})


class ObstacleAPIView(APIView):
    def get(self, request):
        status = request.GET.get('status')
        print(status)
        qs = Obstacles.objects.filter(status=status)
        if qs:
            return Response({'obstacles': ObstaclesSerializer(qs, many=True).data})
        return Response({'message': f'No obstacle with {status} status.'})

    def post(self, request):
        s = ObstaclesSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'obstacle': s.data})
        return Response({'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)

class ObstacleRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Obstacles.objects.all()
    serializer_class = ObstaclesSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            return Response(data={'obstacle': ObstaclesSerializer(instance).data}, status=status.HTTP_200_OK)

        except Obstacles.DoesNotExist:
            return Response(data={'message': 'This obstacle does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Obstacles.DoesNotExist:
            return Response(data={'message': 'This obstacle does not exist'}, status=status.HTTP_404_NOT_FOUND)

        s = ObstaclesSerializer(instance=instance, data=self.request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(data={'obstacle': s.data}, status=status.HTTP_200_OK)
        return Response(data={'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)

class LastDumpAPIView(APIView):
    def get(self, request):
        bot_slug = request.data.get('bot', '')
        qs = LastDump.objects.select_related('bot').filter(bot__slug=bot_slug).order_by('-id').first()
        if qs:
            return Response({'last_dump': LastDumpSerializer(qs).data})
        return Response({'message': "Not enough data"})

    def post(self, request):
        s = LastDumpSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'last_dump': s.data})
        return Response({'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)


class TrashCollectionCentreAPIView(APIView):
    def post(self, request):
        s = TrashCollectionCenterSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'trash_collection_centre': s.data})
        return Response({'message': s.errors}, status=status.HTTP_400_BAD_REQUEST)
