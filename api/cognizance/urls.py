from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers
from django.shortcuts import render


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index')
]