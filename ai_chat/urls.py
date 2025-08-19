from django.urls import path
from . import views

app_name = 'ai_chat'

urlpatterns = [
    path('api/', views.chat_api, name='chat_api'),
]
