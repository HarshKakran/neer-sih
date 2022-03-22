from django.urls import path, include
from .views import BotStatusAPIView, BotListAPIView, TrashAPIView, LastLocationAPIView

urlpatterns = [
    path('bot/', BotListAPIView.as_view(),name='bot_list'),
    path('bot/<str:slug>/', BotStatusAPIView.as_view(), name='bot_status'),
    path('trash/', TrashAPIView.as_view(), name='trash'),
    path('last_location/', LastLocationAPIView.as_view(), name='last_location'),
]
