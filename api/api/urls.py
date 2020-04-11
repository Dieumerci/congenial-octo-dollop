
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import  routers
from cognizance.views import  ItemViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename="item")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('api/', include(router.urls))
    # path('', include('cognizance.urls'))
]
