from django.urls import path, include
from .views import BotStatusAPIView, BotListAPIView, TrashAPIView, LastLocationAPIView \
    , ObstacleAPIView, ObstacleRetrieveUpdateAPIView, LastDumpAPIView, TrashCollectionCentreAPIView

urlpatterns = [
    path('bot/', BotListAPIView.as_view(),name='bot_list'),
    path('bot/<str:slug>/', BotStatusAPIView.as_view(), name='bot_status'),
    path('trash/', TrashAPIView.as_view(), name='trash'),
    path('last_location/', LastLocationAPIView.as_view(), name='last_location'),
    path('obstacle/', ObstacleAPIView.as_view(), name='obstacle'),
    path('obstacle/<str:slug>/', ObstacleRetrieveUpdateAPIView.as_view(), name='obstacle_retrieve_update'),
    path('last_dump/', LastDumpAPIView.as_view(), name='last_dump api'),
    path('trash_collection_centre/', TrashCollectionCentreAPIView.as_view(), name='trash_collection_centre api'),
]
