
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('videos', views.video, name='video'),
    path('gallery', views.gallery, name='gallery'),

]
