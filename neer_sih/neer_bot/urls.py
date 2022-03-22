from django.urls import path, include
from .views import BotStatusAPIView, BotListAPIView, TrashAPIView

urlpatterns = [
    path('bot/', BotListAPIView.as_view(),name='bot_list'),
    path('bot/<str:slug>/', BotStatusAPIView.as_view(), name='bot_status'),
    path('trash/', TrashAPIView.as_view(), name='trash_post')
]
