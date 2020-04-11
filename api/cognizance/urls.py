from django.urls import path, include
from .views import (
            UserViewSet,
            ItemCreateView,
            ItemDestroyView,
            UpdateAPIView
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', ItemCreateView.as_view()),
    path('<pk>/update/', UpdateAPIView.as_view()),
    path('<pk>/delete/', ItemDestroyView.as_view()),
    # path('', views.index, name='index')
]