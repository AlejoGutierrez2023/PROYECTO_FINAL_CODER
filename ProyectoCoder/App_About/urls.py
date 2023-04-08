from django.urls import path
from .views import about
from App_Accounts import views

urlpatterns = [
    path('', about, name='about'),
    path('base', views.base, name='base')
]
