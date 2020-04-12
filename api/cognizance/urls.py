from django.urls import path, include
from .views import (
            UserViewSet,

)
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index')
]