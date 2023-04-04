from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages_list, name='messages_list'),
    path('create/', views.message_create, name='message_create'),
]
