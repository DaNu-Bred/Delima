from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ch1', views.ch1, name='ch1'),
    path('ch2', views.ch2, name='ch2'),
]
