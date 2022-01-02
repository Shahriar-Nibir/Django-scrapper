from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scrap', views.scrap, name='scrap'),
]
