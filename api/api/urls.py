
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import  routers
from cognizance.views import ItemViewSet
router = routers.DefaultRouter()
router.register(r'', ItemViewSet, basename="item")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('api/', include(router.urls))
    # path('', include('cognizance.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
